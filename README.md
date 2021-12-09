# Microsoft Movie Studio Analysis

![img](./images/director_shot.jpeg)

**Authors**: Ashley Eakland


## Overview

I have been tasked with gathering insights for Microsoft as they venture into the movie-making business. My goal is to identify areas and variables in which Microsoft can focus their attention to ensure profitability as they make their leap into this venture. I will analyze the data provided to identify what attributes the top performing films have in common using exploratory data analysis, statistics, and visualizations. Through my analysis, I have been able to identify correlations between film ratings and domestic gross, movie runtimes, and genres. Based on these findings, I have made recommendations to stick within a specific runtime range, aim for highest number of ratings possible, and identified which genres are most likely to be profitable.  

## Business Problem

Microsoft is considering opening a movie studio, but does not have a knowledge base of the film industry, and seeks insight to launch a successful film studio. To assist with this problem, I am analyzing film statistics from the past 11 years to determine which genres of films performed well, and if there are particular reasons why those genres perform well.
***
* Which movie genres performed the best in terms of gross domestic profit?
* What correlations between the top genres and other variables exist (i.e. runtime minutes, average ratings, etc)?

By finding the answers to these questions, I believe I can provide valuable insight to Microsoft to identify the focus areas to best allocate funds and ensure a successful launch.
***

## Data

For this analysis, I am utilizing provided datasets from IMDB and Box Office Mojo so that I may analyze to provide insight to Microsoft as they navigate entry into the movie industry. These datasets represent film statistics and performance both with international and domestic releases, spanning many genres and runtime lengths going back to 2010 and all the way up to films yet to be released. Variables include movie titles, ratings, runtimes, genres, and gross profit. Target variable is going to be profit as the main goal behind any business venture is going to be profitability. 

For the purpose of this analysis, I will eliminate the movies not yet released as they will not serve in the analysis of profitability. I will look at correlations between ratings, runtimes, genres, and gross profit to see where funds are likely to be best allocated.


## Methods

Upon a cursory review of the data, we see that there are missing values in the genre, runtime, and original_title columns in the Titles dataframe. The ratings dataframe is complete. The gross profit dataframe is also missing values in both the domestic and gross profit columns. To first identify what columns and values can be dropped, I will need to combine my dataframes for analysis with profit, as profit is my target variable.

***

* I did discover many duplicate values that were throughout the dataframe. I identified the duplicates, found the first instance in the set (identified release year and profit) and dropped the duplicated titles. I dropped the "original title" column from the dataset for cleanliness as I didn't need that column for my analysis.
* For the null values in the dataset, runtime minutes was missing about 10% of it's total values. Through analysis, I determined that the median would be the suitable option to fill the null values. Additionally, domestic gross was missing a small percent (less than 1%) of it's values. By taking a closer look at those 22 titles showing null values, I determined that those did have foreign_gross values, so I decided to break those out into the foreign film dataframe to be analyzed with the foreign films. Lastly, there were missing values in the genres column. Given the size of the dataset, overall percentage of missing was just over 1%. Furthermore, I would be unable to fill these values with a "common" genre as every film is so different and could fit into a multitude of genres. For these reasons, I opted to drop those values.
* I did limit the number of values in this sample on my initial combined and sorted dataframe of rated titles to 15003 in order to collect a meaningful value of reviewed films. I sorted my values by the number of votes, and then by the average rating to get films that had at least 429 ratings. 429 ratings may still be a little low in terms of votes by viewers, but I wanted a larger sample as a starting point for analysis. I did further narrow this scope as my analysis progressed.

### Data Modeling
As I completed my cleaning steps of the dataframes, I utilized the visualizations below to see the correlations that exist between the variables in the datasets.

* Using the top grossing films, I was able to see which genres performed the best at the box office in terms of gross domestic profit when compared to just the top 100 films in this set. To try and corroborate this, I analyzed the genres from the top ranking films by also graphing the top 100 ranked films by their genres, and we do see some commonalities in the genres that appear. Additionally, I wanted to analyze correlations between runtimes and ratings, and ratings and profits, as both may seem to have weight on box office performance.
* Since many of my questions involve two variables, models used were primarily scatter plots and bar graphs, analyzed by the relationship between the two graphed variables and based upon the cleaned data prepared for modeling. I did utilize heatmaps as well, which are a concise and different way to see the correlations shown in the scatter plots.
I continuously scoured my data to ensure that it was clean and complete, watching for potential correlations or questions to jump out as I progressed through. I made numerous dataframe copies so that I could run various trials without risk of ruining existing tables or graphs.


## Results

***

### Genre
![graph1](./images/top_grossing_genres.png)
![graph2](./images/top_ranking_genres.png)

Top grossing films are in the Adventure, Action, Comedy, Sci-Fi, Animation, Fantasy, Thriller, Drama and Crime genres respectively, among others listed. Genres were difficult to analyze in this dataset due to the structure, and I would like additional time to reassess genre specific data for more specific recommendations pertinent to genre.

### Movie Length
![graph3](./images/avg_rating_runtime.png)
![graph4](./images/num_votes_runtime.png)

Positive correlations associated with both average movie rating and movie runtime as well as the number of votes and movie run time.  Number of ratings are a critical variable in evaulating the average rating as with a low number of ratings, the average rating data will be skewed. 

### Rating Importance
* Higher number of ratings tend to correlate with higher profit. More people seeing and rating the movie would equate to more profitability. 
![graph5](./images/heat_map_profit.png)
![graph5](./images/num_ratings_profit.png)

* This data could be generalized beyond the data possessed. I believe that while the results I have extrapolated from my analysis are broad in terms of recommendations, they are supported and could be replicated with similar or additional data. I would like to see a dataset with single genres rather than mixed or multiple genres per title as that really has the potential to skew counts and analysis using genre as a variable.

# Conclusions
Limitations of this analysis would be the lack of insight into genre specificity. I would like to dive deeper into the genres and how they relate with ratings and profitability at a later date if the time allows. 

### Business Recommendations
 -Focus on the genres of Adventure, Action, Comedy, Sci-Fi, Animation, Drama, Thriller, Fantasy, and Biography. These genres appear on all of the top ranking films domestically. While the Biography genre does not appear on the top grossing genre count, it does appear relatively high up on the rank of top ranked genres. With a positive correlation between number of ratings and gross profit, I would recommend considering including Biography as a genre or subgenre on your menu as the viewers appear to like them. 
 
 -As previously stated, ratings are important. There is a positive correlation between higher number of ratings and higher profit. We want to maximize on the number of ratings we are getting as that has a stronger direct correlation to gross profit than average rating, which would logically make sense. Each "vote" is one ticket at the box office, and we want as many ratings as possible.
 
 -Lastly, with a positive correlation between run time and average movie rating coupled with the shown positive correlation between movie runtime and ratings, I would recommend sticking around 100 minutes of runtime for optimal movie performance. 
 
* What are some reasons why your analysis might not fully solve the business problem? 
    My analysis may not fully solve the problem as it does not break down which genre specifically is most profitable or which genre specifically ranks the highest due to the challenges I faced.

* What else could you do in the future to improve this project?
     More depth and detailed analysis into genres and their relationships with other variables would definitely be insightful.
***

## For More Information

Please review my full analysis in [my Jupyter Notebook](./dsc-phase1project-microsoftmoviestudioanalysis-eakland.ipynb) or my [presentation](./DS_Project_Presentation_Eakland.pdf).

For any additional questions, please contact **Ashley Eakland, ashley@eakland.net**

## Repository Structure

```
├── README.md                                               <- The top-level README for reviewers of this project
├── dsc-phase1-microsoftmoviestudioanalysis-eakland.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation_Eakland.pdf                     <- PDF version of project presentation
├── data                                                    <- Both sourced externally and generated from code
└── images                                                  <- Both sourced externally and generated from code
```
