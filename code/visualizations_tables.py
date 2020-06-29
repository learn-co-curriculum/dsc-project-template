""" This package contains the functions and settings used to create tables for the animal_shelter_needs_analysis"""

# Standard data manipulation packages
import pandas as pd
import numpy as np

# Is a python wrapper for wkhtmltoimage. would need to install wkhtmltoimage to have it work locally 
# Note - I've only seen this work on Macs, there is some trouble getting it to work with PCs
import imgkit

# Image manipulation packages. PIL stands for Pillow. you need to `pip install Pillow`
import PIL
from PIL import Image, ImageOps


""" The css works with the pandas.dataframe.style object to data summaries be formatted nicely"""


# Css for table style
tb_styles = {'selector': 'table',
            'props':[('margin','0')]}

# Css for table headers
th_styles = {'selector': 'th', 
             'props': [('border', "1"),
                     ("border-color", "black"),
                     ('border-style','solid'),
                     ('border-width','1px'),
                     ('font-family', 'verdana'),
                     ('white-space', 'nowrap'),
                       ('width', '75%'),
                     ("text-align", "left")]}

# Css for data rows
td_styles = {'selector': 'td',
             'props': [('font-family', 'verdana'),
                       ('border', "1"),
                       ("border-color", "black"),
                       ('border-style','solid'),
                       ('border-width','1px'),
                       ('white-space', 'nowrap'),
                       ('padding-right',"10px"),
                       ('padding',"10px")]}

# Css for table title
cap_style = {'selector':'caption',
             'props':[('font-family', 'verdana'),
                      ('white-space', 'nowrap'),
                      ("font-size", "large"),
                     ('padding-bottom',"10px")]}

options = {'quiet': ''}



def value_counts_table(vc_obj, caption_txt, file_name):
    """This function:
        - takes a pd.Series output from value_counts() and converts it to a pd.DataFrame
        - formats the css and html to make it look nice
        - renders the html
        - converts the html to a PNG file
        - crops the image
        - saves the updated image file
        
        
        Parameters
        ----------
        vc_obj : series
            Output from a summary table created by using value_counts()
        caption_txt : string
            Title of table
        file_name : string
            what you want the file to be named
        
        Returns
        -------
        file_name.png : saves image of converted value_counts output"""    
        
    # Takes a pd.Series output from value_counts() and converts it to a pd.DataFrame        
    test_df =vc_obj.to_frame()        
    test_df.columns = ["count"]

    # Formats the css and html to make it look nice
    improved = test_df.style.format('{:,.0f}').set_table_attributes('style="border-collapse:collapse"')\
                     .set_table_styles([tb_styles, th_styles,td_styles,cap_style]).set_caption(caption_txt)
    # Renders the html
    html = improved.render()

    # Renders the html & saves as image
    path = './images/'+file_name+'.png'
    imgkit.from_string(html, path, options=options)

    # Crops the image
    
    ## PIL opens image
    im = Image.open(path)
    
    ## Inverts the colors of the image, because getbbox looks for black boundaries, not white ones
    inverted = ImageOps.invert(im.convert('RGB'))
    
    ## Get the automated boundaries box from the inverted file
    boxed = inverted.getbbox()
    
    ## Slaps those crop boundaries on the orginal image
    cropped_image=im.crop(boxed)

    # BAM, saves the cropped image file over the orignal
    cropped_image.save(path)
    pass

def df_table_percents(df_obj, caption_txt, file_name):
    """This function:
        - takes a pd.DataFrame as input
        - formats the css and html to make it look nice
        - renders the html
        - converts the html to a PNG file
        - crops the image
        - saves the updated image file
        
        
        Parameters
        ----------
        df_obj : dataframe
           input dataframe
        caption_txt : string
            Title of table
        file_name : string
            what you want the file to be named
        
        Returns
        -------
        file_name.png : saves image of converted value_counts output"""
    test_df = df_obj.copy()
    test_df.columns = test_df.columns.str.title()
    
    # Css for table title
    cap_style2 = {'selector':'caption',
             'props':[('font-family', 'verdana'),
                      ("font-size", "large")]}
    
    
    # Css for data rows
    td_styles2 = {'selector': 'td',
             'props': [('font-family', 'verdana'),
                       ('border', "1"),
                       ("border-color", "black"),
                       ('border-style','solid'),
                       ('padding',"5px"),
                       ('border-width','1px')]}
    
    th_styles2 = {'selector': 'th', 
             'props': [('border', "1"),
                     ("border-color", "black"),
                     ('border-style','solid'),
                     ('border-width','1px'),
                     ('white-space', 'nowrap'),
                     ('font-family', 'verdana'),
                     ("text-align", "left"),
                       ('padding-right',"10px"),
                       ('padding',"10px")]}


    # Formats the css and html to make it look nice
    improved = test_df.style.format("{:.2%}").set_table_attributes('style="border-collapse:collapse"')\
                     .set_table_styles([tb_styles, th_styles2,td_styles2,cap_style2]).set_caption(caption_txt)
    # Renders the html
    html = improved.render()

    # Renders the html & saves as image
    path = './images/'+file_name+'.png'
    imgkit.from_string(html, path, options=options)

    # Crops the image
    
    ## PIL opens image
    im = Image.open(path)
    
    ## Inverts the colors of the image, because getbbox looks for black boundaries, not white ones
    inverted = ImageOps.invert(im.convert('RGB'))
    
    ## Get the automated boundaries box from the inverted file
    boxed = inverted.getbbox()
    
    ## Slaps those crop boundaries on the orginal image
    cropped_image=im.crop(boxed)

    # BAM, saves the cropped image file over the orignal
    cropped_image.save(path)
    pass


