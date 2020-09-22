"""
This module is for your data cleaning.
It should be repeatable.
If you are combining different data sources you might need a few different functions

## Data links:


## SUPPORT FUNCTIONS
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd

def support_function_one(example):
    """This one might read in the data from imdb and clean it"""
    return example

def support_function_two(example):
    """This function might read in and clean a different data source"""
    return example

def support_function_three(example):
    """This one might merge the above two sources and create a few new variables"""
    return example

def full_clean():
    """
    This is the one function called that will run all the support functions.
    Assumption: 
        - Your data files will be saved in a data folder and named "dirty_data.csv"
        - OR you might read directly from a few urls
        - this code is guidance, not rules

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    dirty_data = pd.read_csv("./data/dirty_data.csv")

    cleaning_data1 = support_function_one(dirty_data)
    cleaning_data2 = support_function_two(cleaning_data1)
    cleaned_data= support_function_three(cleaning_data2)
    cleaned_data.to_csv('./data/cleaned_for_testing.csv')
    
    return cleaned_data