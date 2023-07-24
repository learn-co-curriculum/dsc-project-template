# Microsoft Movie Analysis

**Author**: Sylvester Magunda

## Overview

This project uses EDA to generate insights for Microsoft, which wants to start a new movie studio. Based on Box Office Mojo and IMDB data, recommendations are made on what Microsoft should consider before creating the studio. This model uses metrics such as worldwide gross income over the years, number of movies in specific languages, genre_ids with most movies, and average vote to help Microsoft make informed decisions. Generally, the findings show that Microsoft should produce movies in English. Results also show that worldwide gross income has been increasing since 2015.

## Business Problem

Microsoft, realizing the proliferation of original video content production among leading companies, has decided to start a movie studio. However, they hardly have any information about movie production. This project explores the data to identify significant details to help Microsoft make informed decisions while creating the new studio.
This analysis responds to the following questions:
* What is the number of movies per original language?
* What is the relationship between production budget and profits?
* What is the average rating per original language?
* How has worldwide gross income been changing over the years?
* What is the relationship between the original language and the vote average?

## Data

This project is based on Box Office Mojo and IMDB data to understand the best-performing movies. The data used represent information on different movies using columns such as original_language, title, genre_ids, wordwide_gross, vote_average, and production_budget, which are all important in making informed decisions on movie production.

## Methods

This project uses descriptive analysis, including a description of gross income over time. This offers a suitable overview of the growth of the movie production sector and possible ways for Mircosoft to fit in it. 

## Results

From my model, the results are as follows:
* Worldwide gross income has been increasing since 2015
* There is a positive linear relationship between profits and the production budget
* The "vote_count" column has some outliers
* Most movies are averagely voted at around 6.5 
* Most movies produced are for genre_id "[18]"
* Most movies are produced in the English language

The introduction of theatres and streaming video companies such as Netflix are probably the reasons for the increase in worldwide gross income. Currently, producing a high-quality movie does not come cheap; even after its production, some good money must be spent on marketing and advertising. Therefore, movie producers should consider a reasonable production budget to maximize profits. The average vote is around 6.5, which shows how people appreciate movies of almost all genres and that every movie has its audience. I am confident with this model because it focuses on minor details like original language, which will help Microsoft decide on the language of their movies. However, language does not determine how movies are rated, probably because of captions and people watching movies with languages they understand.
Visual 1
Worldwide gross income has been increasing since 2015
 
Visual 2
Top 10 most used studios in movie production
 


### Visual 1
![graph1](./images/viz1.png)

## Conclusions

In conclusion, this model presents a major opportunity for Microsoft to invest in the movie production business and tap into the growing demand for original video content leading to increased worldwide gross income since 2015. Microsoft can make informed decisions about the types of movies to produce, ensuring the success of their new movie studio. Since more than 90% of movies in my dataset are in English, Microsoft should focus on producing English movies. Microsoft should also invest heavily in production to realize good profits. Finally, there is a list of my project's top 10 movie production studios that Microsoft can consider collaborating with or benchmark from.
One of the main limitations of my project is that my data missed the genre columns but instead had genre ids, so I did not focus much on the genre. However, from my shallow analysis of genre_ids, Microsoft should focus on producing movies of genre_id 18. The issue is that my data could not define the genre's name. Therefore, there's a need for genres in future work, and more research should be done on how those genres relate to their specific worldwide gross income. Apart from theatrical earnings, studios can earn revenue through streaming services, television rights, home entertainment sales and 

## For More Information

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **name & email, name & email**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── __init__.py                         <- .py file that signals to python these folders contain packages
├── README.md                           <- The top-level README for reviewers of this project
├── dsc-phase1-project-template.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── code
│   ├── __init__.py                     <- .py file that signals to python these folders contain packages
│   ├── visualizations.py               <- .py script to create finalized versions of visuals for project
│   ├── data_preparation.py             <- .py script used to pre-process and clean data
│   └── eda_notebook.ipynb              <- Notebook containing data exploration
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
