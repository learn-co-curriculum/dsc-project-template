"""
This package of functions takes the output from the data_cleaning.py package as an input. 
It assumes those funtions have been run on Austin Animal Center datasets.

This package includes the following functions:
- create_species_var
- create_neutered_var
- reduce_breed_list
"""

import pandas as pd
import numpy as np


##### Create new variable SPECIES ##### 
def create_species_var(test):
    """
    The function create_species_var takes a cleaned, merged, dataset as an argument
    returns dataset with a new variable "species" that gives more granularity than
    animal_type and less refined than breed.
    """
    
    # Default value of species with low count
    test['species'] = "Other"

    # Mapping of breeds to species to provide more granularity than animal_type
    # These list names might need to be in all caps, since they are "contsants"
    # Will see what the linter returns
    rabbit_breeds = ["Silver","Britannia","Zealand","Cinnamon","Belgian",'Hotot', 
                     "Cottontai","Rhinelander","Flemish","Rabbit", "Lop", "English Spot",
                     'Checkered', "Californian", "Rex", "American", "Angora", "Lionhead",
                     "Dwarf", "Dutch", "Havana","Himalayan","Jersey", "Polish", 'Harlequin']
    reptile = ["Snake", "Tortoise", "Turtle","Lizard"]
    wildlife = ["Squirrel", "Fox", "Skunk","Raccoon", "Bat", "Ringtail", "Opossum", "Coyote", "Armadillo"]
    aquatic = ["Crab", "Tropical", "Cold Water"]
    rodent = ['Mouse', "Rat", "Hamster", "Gerbil", "Chinchilla", 'Prairie']
    chicken = ["Chicken", "Bantam", 'Silkie',"Rhode", "Orpington","Leghorn","Barred"]
    duck = ["Muscovy", "Duck"]
    parrot = ["Budgerigar", "Parrot", "Conure", "Quaker", "Macaw", 
              "Cockatoo","Cockatiel","African","Lovebird", "Parakeet"]
    game_bird = ["Pheasant","Turkey","Peafowl"]
    song_bird = ["Canary", "Finch", "Sparrow", "Dove", "Pidgeon"]


    ##### Asigning values to species ######


    # Coding main categories
    test.loc[test['animal_type']=="Cat", 'species'] = 'Cat'
    test.loc[test['animal_type']=="Dog", 'species'] = 'Dog'
    test.loc[test['animal_type']=="Livestock", 'species'] = 'Livestock'

    # Coding wildlife - part 1
    test.loc[(test['animal_type']=="Bird") \
            & (test['intake_type'] == 'Wildlife'), 'species'] = 'Wildlife'
    test.loc[(test['animal_type']=="Bird") \
            & (test['intake_type'] != 'Wildlife') \
            & (test.breed.str.contains("Hawk")), 'species'] = "Wildlife"

    # Bird coding
    test.loc[(test['animal_type']=="Bird") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(chicken))),'species'] = "Chicken"
    test.loc[(test['animal_type']=="Bird") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(duck))), 'species'] = "Duck" 
    test.loc[(test['animal_type']=="Bird") \
            & (test['intake_type'] != 'Wildlife') \
            & test['breed'].str.contains("|".join(parrot)), 'species'] = "Parrot"
    test.loc[(test['animal_type']=="Bird") \
            & (test['intake_type'] != 'Wildlife') \
            & test['breed'].str.contains("|".join(song_bird)),'species'] = "Song Bird"
    test.loc[(test['animal_type']=="Bird") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(game_bird))), 'species'] = 'Game Bird'

    # Coding other category
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] == 'Wildlife'), 'species'] = 'Wildlife'
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(wildlife))), 'species'] = 'Wildlife'
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("Hedge")), 'species'] = "Hedgehog"
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("Guinea")), 'species'] = "Guinea Pig"
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("Ferret")), 'species'] = "Ferret"
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(reptile))), 'species'] = "Repitle"
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(rabbit_breeds))), 'species'] = "Rabbit"
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(rodent))), 'species'] = "Rodent"
    test.loc[(test['animal_type']=="Other") \
            & (test['intake_type'] != 'Wildlife') \
            & (test['breed'].str.contains("|".join(aquatic))), 'species'] = 'Aquatic'
    return test

def create_neutered_var(test):
    """ 
    Input: cleaned dataset
    returns: dataset with added variable "neutered"
    Compares the sex_upon_intake and sex_upon_outcome to see if the status changed while with the center
    Chose a 1/0 encoding to allow sums
    """
    
    ### Create Neutering variable
    test['neutered'] = np.where(test.sex_upon_intake != test.sex_upon_outcome, 1, 0)
    
    return test


def reduce_breed_list(test):
    """
    Input: cleaned dataset
    returns: a data set with the variable "breeds" reduced for cats and dogs. 
    
    Removes the "Mix" part of the breed name and stripped white space.
    Made choice that Domestic Shorthair is equivalent to Domestic Shorthair Mix when it comes to cats
    """
    
    # Fix cat breeds
    test.loc[(test['species']=="Cat")& (test.breed.str.contains('Mix')), 'breed'] = test.breed.str.replace("Mix", "")
    test.loc[(test['species']=="Cat"), 'breed'] = test.breed.str.strip()

    # Fix dog breeds
    test.loc[(test['species']=="Dog")& (test.breed.str.contains('Mix')), 'breed'] = test.breed.str.replace("Mix", "")
    test.loc[(test['species']=="Dog"), 'breed'] = test.breed.str.strip()
    
    return test