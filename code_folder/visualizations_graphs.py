""" This package contains the functions and settings used to create graphs for the animal_shelter_needs_analysis"""

# visualization packages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib.cm as cm

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

def time_series_plot(dataset,title,xlab,ylab,file_name, y_tick_num):
        """This function:
        - takes a pd.Series output from value_counts() and converts it to a pd.DataFrame
        - formats the css and html to make it look nice
        - renders the html
        - converts the html to a PNG file
        - crops the image
        - saves the updated image file
        
        
        Parameters
        ----------
        dataset : DataFrame
            Output from a summary table created by using value_counts()
        title : string
            Title on graph
        xlab : string
        ylab : string
        file_name : string
            what you want the image file to be named

        Returns
        -------
        file_name.png : saves image of matplotlib output"""
        
        
    
        # assign argument values to variables
        file_name = file_name
        title = title
        xlab = xlab
        ylab = ylab
        data = dataset.copy()

        # Create figure container
        fig = plt.figure(figsize=(16, 10), dpi=80) 


        # Creates one subplot within our figure and uses the classes fig and ax
        fig, ax = plt.subplots(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
        
        color=cm.rainbow(np.linspace(0,1,len(data.columns.tolist())))

        # Loops through species catagory and adds them to the plot
        for col_name, c in zip(data.columns.tolist(),color):
            ax.plot(data.index, col_name, data=data, linewidth=4,c=c)

        # Format the ticks

        ## X Axis    
        ### Specify variables I want to use
        years = mdates.YearLocator()   # every year
        months = mdates.MonthLocator(interval=3)  # every month
        years_fmt = mdates.DateFormatter('%b-%Y')
        mon_fmt = mdates.DateFormatter('%b')

        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(years_fmt)
        ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
        ax.xaxis.set_minor_formatter(mon_fmt)

        ## Y Axis format
        ax.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_num))
        
      
        string_format = '{x:,.0f}'
        
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter(string_format))

        # Sets the limits of the x-axis: round to nearest years.
        datemin = np.datetime64(data.index.min(), 'Y')
        datemax = np.datetime64(data.index[-1], 'Y') + np.timedelta64(1, 'Y')
        ax.set_xlim(datemin, datemax)

        # Dynamically sets a bunch of labels
        ax.set_title(title)
        ax.set_xlabel(xlab)
        ax.set_ylabel(ylab)
        ax.legend()

        # Specifies I want the grid for BOTH level of tick marks
        ax.grid(True, which="both")

        # rotates and right aligns the x labels, and moves the bottom of the
        # axes up to make room for them
        fig.autofmt_xdate(which='both')

        path = './images/'+file_name+'.png'
        plt.savefig(path)
        plt.close(fig)  
        pass
    
"""Same thing as above except with percent formatting"""    
def time_series_plot_percent(dataset,title,xlab,ylab,file_name, y_tick_num):
        """This function:
        - takes a pd.Series output from value_counts() and converts it to a pd.DataFrame
        - formats the css and html to make it look nice
        - renders the html
        - converts the html to a PNG file
        - crops the image
        - saves the updated image file
        
        
        Parameters
        ----------
        dataset : DataFrame
            Output from a summary table created by using value_counts()
        title : string
            Title on graph
        xlab : string
        ylab : string
        file_name : string
            what you want the image file to be named

        Returns
        -------
        file_name.png : saves image of matplotlib output"""
        
        
    
        # assign argument values to variables
        file_name = file_name
        title = title
        xlab = xlab
        ylab = ylab
        data = dataset.copy()

        # Create figure container
        fig = plt.figure(figsize=(16, 10), dpi=80) 


        # Creates one subplot within our figure and uses the classes fig and ax
        fig, ax = plt.subplots(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
        
        color=cm.rainbow(np.linspace(0,1,len(data.columns.tolist())))

        # Loops through species catagory and adds them to the plot
        for col_name, c in zip(data.columns.tolist(),color):
            ax.plot(data.index, col_name, data=data, linewidth=4,c=c)

        # Format the ticks

        ## X Axis    
        ### Specify variables I want to use
        years = mdates.YearLocator()   # every year
        months = mdates.MonthLocator(interval=3)  # every month
        years_fmt = mdates.DateFormatter('%b-%Y')
        mon_fmt = mdates.DateFormatter('%b')

        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(years_fmt)
        ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
        ax.xaxis.set_minor_formatter(mon_fmt)

        ## Y Axis format
        ax.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_num))
        
      
        
        ax.yaxis.set_major_formatter(ticker.PercentFormatter())

        # Sets the limits of the x-axis: round to nearest years.
        datemin = np.datetime64(data.index.min(), 'Y')
        datemax = np.datetime64(data.index[-1], 'Y') + np.timedelta64(1, 'Y')
        ax.set_xlim(datemin, datemax)

        # Dynamically sets a bunch of labels
        ax.set_title(title)
        ax.set_xlabel(xlab)
        ax.set_ylabel(ylab)
        ax.legend()

        # Specifies I want the grid for BOTH level of tick marks
        ax.grid(True, which="both")

        # rotates and right aligns the x labels, and moves the bottom of the
        # axes up to make room for them
        fig.autofmt_xdate(which='both')

        path = './images/'+file_name+'.png'
        plt.savefig(path)
        plt.close(fig)  
        pass 