""" This package contains the functions and settings used to create boxplots for the animal_shelter_needs_analysis"""

# visualization packages
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import numpy as np

import seaborn as sns

from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')



""" Setting parameters for matplotlib outside of the function, since I will reuse them multiple times
    It's also something I can quickly copy and paste from one script to another, personal preference"""

# Set specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'xtick.minor.bottom':True,
          'ytick.labelsize': med,
          'figure.titlesize': large}



# Set style parameters
sns.set_style("ticks", { 'axes.spines.top': False, 'axes.spines.right': False, "xtick.major.size": med, "xtick.minor.size": 8, 'axes.titlesize': large, 'ytick.labelsize': med})
plt.rcParams.update(params)



def breed_days_in_shelter(dataset, file_name):
    
    test = dataset.loc[(dataset.species=="Dog") &(dataset.year==2019) & (dataset.outcome_type =="Adoption")]
    breeds_sub = test.breed.value_counts()[:15]
    breed_list = breeds_sub.index.to_list()

    medians= test.loc[test.breed.isin(breed_list)].groupby(['breed'])["days_in_shelter"].quantile(q=.75)
    medians.sort_index(inplace=True)

    nobs = test.loc[test.breed.isin(breed_list)]["breed"].value_counts().values
    nobs = [str(x) for x in nobs.tolist()]
    nobs = ["n: " + i for i in nobs]

    fig = plt.figure(figsize=(16, 10), dpi=80) 

    # Creates one subplot within our figure and uses the classes fig and ax
    fig, ax = plt.subplots(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
    chart = sns.boxplot( x=test.loc[test.breed.isin(breed_list)].sort_values(by=['breed'])["breed"], y=test.loc[test.breed.isin(breed_list)].sort_values(by=['breed'])["days_in_shelter"],color='w', showfliers=False )
    #ax.xaxis.set_major_locator()
    plt.xticks(rotation=45, 
        horizontalalignment='right')
    #ax.set_ylim(0, 100)
    # Add it to the plot
    pos = range(len(nobs))
    for tick,label in zip(pos,ax.get_xticklabels()):
        ax.text(pos[tick], medians[tick]+ 0.03, nobs[tick], horizontalalignment='center', size='large', color='black', weight='semibold')

    ax.set_title("Distribution of days spent in shelter before adoption")
    ax.set_xlabel("Dog breeds")
    ax.set_ylabel("Days spent in shelter")
    
    plt.tight_layout()
    
    path = './images/'+file_name+'.png'
    plt.savefig(path)
    plt.close(fig)  
    pass


def dist_plot_cats_dogs(data, file_name):
    cats = data.loc[(data.species=="Cat") &(data.year==2019) & (data.outcome_type =="Adoption")].days_in_shelter
    dogs = data.loc[(data.species=="Dog") &(data.year==2019) & (data.outcome_type =="Adoption")].days_in_shelter
    
    fig = plt.figure(figsize=(16, 10), dpi=80) 
    
    # plot dist plot for cats with annotation
    sns.distplot(cats, hist = False, kde = True,
                     kde_kws = {'linewidth': 3,'alpha':0.3, 'shade':True},
                     label = "Cats")
    plt.axvline(cats.mean(), color='blue', linestyle='dashed', linewidth=2)
    min_ylim, max_ylim = plt.ylim()
    plt.text(cats.mean()*1.1, max_ylim*0.9, 'Mean days in shelter\n for cats: {:.2f}'.format(cats.mean()))

    # plot overlapping dist plot for dogs with annotation
    sns.distplot(dogs, hist = False, kde = True,
                     kde_kws = {'linewidth': 3,'alpha':0.3, 'shade':True},
                     label = "Dogs")
    plt.axvline(dogs.mean(), color='orange', linestyle='dashed', linewidth=2)
    min_ylim, max_ylim = plt.ylim()
    plt.text(dogs.mean()*.4, max_ylim, 'Mean days in shelter\n for dogs: {:.2f}'.format(dogs.mean()))

    plt.title("Days in shelter before adoption for cats and dogs")
    plt.legend(loc='upper right')
    plt.xlabel("Days in shelter before adoption")

    path = './images/'+file_name+'.png'
    plt.savefig(path)
    plt.close(fig)  
    pass