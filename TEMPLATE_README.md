# Title

**Author**: Karen Ballard

## Overview

Microsoft have decided to create a new movie studio and require more insight into which types of films are doing best at the box office. This project uses descriptive statistical analysis on data gathered from IMDb website to gain insight into which combination of genres topped the league in these areas. Three seperate datasets were used for this analysis to gain insight into which combination genres of movies topped the domestic gross sales, foreign gross sales, had the top average ratings and number of votes. The results of the top 20 combination genres in Domestic Sales, Foreign Sales and number of votes was clearly the combination Action, Adventure & Sci-Fi, with adventure being present in the majority of the top 20 of the 3 categories. My recommendation for which type of Movie to produce would be Action, Adventure & Sci-Fi as this is the most predominant combination in the analysis, there were 260 unique genre combinations in this data set after cleaning. I would also highly recommend that Adventure and Action paired with either Animation or Fantasy is a successful combination. In Domestic and Foreign Sales the combination Adventure, Animation & Comedy also faired well which would be my third recommendation. Adventure was clearly a strong genre for popular successful movies.

## Business Problem

Microsoft want to produce movies that are going to be successful in order to make profits, they want to know which types of movies are the most successful. To answer that question both Domestic and Foreign Sales data was analysed to see the most financially successful genres, along with the average rating given and number of votes for each type or genre of movie to see how popularity compared with financial success.


***

## Data

Describe the data being used for this project.

***
Questions to consider:
* Where did the data come from, and how do they relate to the data analysis questions?
* What do the data represent? Who is in the sample and what variables are included?
* What is the target variable?
* What are the properties of the variables you intend to use?
***

## Methods

The data analysed came from IMDb website. IMDb (an acronym for Internet Movie Database) is a popular worldwide online database of infomation relating to all movies, television programs, video games and streaming content online. I used 3 files from IMDb to answer the question of which genres were most successful, mainly focusing on the Domestic and Foreign Gross sales along with average ratings given and number of votes received.Describe the process for analyzing or modeling the data.

***
After checking the information on each table to see column names and null values, I joined the two datasets, df_titles_basic_info and df_ratings together using the 'tconst' column as it was a unique identifier creating a new dataframe called joinedimdb. I then joined the dataset df_movie_gross with the new dataframe using the title as the unique identifier, creating a combined new dataset called complete_df.

Checking the information on the new dataframe complete_df, I then cleaned up the null values by removing them, tidied up the "Domestic Gross' and 'Foreign Gross' columns and converted them to units of $ millions for easier readability and analysis. The columns"studio", "original title", and the original domestic and foreign gross columns were deleted as they were not required to carry out this analysis.
***

## Results

Present your key results. For Phase 1, this will be findings from your descriptive analysis.

***
Questions to consider:
* How do you interpret the results?
* How confident are you that your results would generalize beyond the data you have?
***

Here is an example of how to embed images from your sub-folder:

### Visual 1
![graph1](./images/viz1.png)

## Conclusions

Provide your conclusions about the work you've done, including any limitations or next steps.

***
Questions to consider:
* What would you recommend the business do as a result of this work?
* What are some reasons why your analysis might not fully solve the business problem?
* What else could you do in the future to improve this project?
***

## For More Information

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **name & email, name & email**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── README.md                           <- The top-level README for reviewers of this project
├── dsc-phase1-project-template.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
