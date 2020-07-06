"""
This package of functions cleans the raw data from the Austin Animal Center datasets.
It includes:
- prep_outcomes_file
- prep_intakes_file
- merge_files
"""

import pandas as pd
import numpy as np

## Clean Outcomes

def prep_outcomes_file(outcomes):
    """The raw file comes in with: 
    - dates not in datetime format
    - column names have mixed cases and spaces
    - an age variable that needs to be replaced
    - unnecessary columns tht can be dropped
    - create some additional date variables to help merge later
    
    arguments
    outcomes: the raw file from the website
    returns clean dataset"""
    # Make column names easier to use
    outcomes.columns = outcomes.columns.str.lower()
    outcomes.columns = outcomes.columns.str.replace(' ', '_')

    # Convert date formats
    outcomes['date_o'] = outcomes.datetime.apply(lambda x: x[:10])

    outcomes['date_o'] =  pd.to_datetime(outcomes['date_o'], format='%m/%d/%Y')
    outcomes['dob'] =  pd.to_datetime(outcomes['date_of_birth'], format='%m/%d/%Y')

    # Create new age variable
    outcomes['age'] = outcomes.date_o - outcomes.dob
    outcomes['years_old'] = outcomes.age.apply(lambda x: x.days/365)

    outcomes['year'] = outcomes['date_o'].apply(lambda x: x.year)

    outcomes['month_o'] = outcomes['date_o'].apply(lambda x: x.month)
    outcomes['year'] = outcomes['date_o'].apply(lambda x: x.year)
    outcomes['weekday_o'] = outcomes['date_o'].apply(lambda x: x.weekday())

    outcomes.drop(columns = ['datetime', 'date_of_birth','age_upon_outcome', 'date_of_birth',  'breed', 'color','animal_type'], inplace=True )
    return outcomes


# Let's repeat the cleaning process for intake date and create some new variables

def prep_intakes_file(intakes):
    """The raw file comes in with: 
    - dates not in datetime format
    - column names have mixed cases and spaces
    - unnecessary columns tht can be dropped
    - create some additional date variables to help merge later
    
    arguments
    intakes: the raw file from the website
    returns clean dataset"""

    # Update column names to be more friendly

    intakes.columns = intakes.columns.str.lower()
    intakes.columns = intakes.columns.str.replace(' ', '_')

    # Convert date formats
    intakes['date_i'] = intakes.datetime.apply(lambda x: x[:10])

    intakes['date_i'] =  pd.to_datetime(intakes['date_i'], format='%m/%d/%Y')

    # Create more date variables
    intakes['month_i'] = intakes['date_i'].apply(lambda x: x.month)
    intakes['year'] = intakes['date_i'].apply(lambda x: x.year)
    intakes['weekday_i'] = intakes['date_i'].apply(lambda x: x.weekday())

    intakes.drop(columns =['datetime','monthyear','age_upon_intake'] , inplace = True)
    return intakes

def merge_files(intakes, outcomes):
    """
    Merges intakes and outcomes datasets to create unique line for each animal in the shelter to capture full stories for each animal
    takes intakes file then outcomes file as arguments
    returns merged dataset
    """
   # Merge intakes and outcomes on animal id and year
    animal_shelter_df  = pd.merge(intakes, 
                                  outcomes, 
                                  on=['animal_id', 'year'], 
                                  how='left', 
                                  suffixes=('_intake', '_outcome'))

    # Filters out animals who have yet to have outcomes and keeps animals where outcome data is later than intake date
    animal_shelter_df = animal_shelter_df[(~animal_shelter_df['date_o'].isna()) 
                                          & (animal_shelter_df['date_o'] > animal_shelter_df['date_i'])]
    
    # Sorts the column names to be alphabetical
    animal_shelter_df = animal_shelter_df[animal_shelter_df.columns.sort_values()]
    return animal_shelter_df
