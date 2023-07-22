
---

![Vintage Movie Cassette Tape](https://media.discordapp.net/attachments/1008571220385599488/1126232701146501360/MadsMeyer_peaky_blinders_style_painting_2e662a64-2009-46fd-b8bf-12e84648efc4.png?width=573&height=573)

# Movie Analysis: A Deep Dive into Box Office Performance

**Author**: [Oscar Mulei](mailto:omulei@gmail.com)

## Overview

This project provides a comprehensive analysis of box office performance for movies. The goal is to offer valuable insights to Microsoft's newly established movie studio. The analysis covers various aspects of movies, such as genres, ratings, budgets, and release dates, to uncover the factors that contribute to a successful box office performance.

## Business Problem

![img](https://media.discordapp.net/attachments/1050435586235846767/1052697908295774298/yassein_muhamedddd_action_movie_poster_movie_poster_action_movi_5d7ba72b-db05-4212-917c-85855d4425c1.png?width=573&height=573)

Microsoft, recognizing the success of other big companies in creating original video content, is eager to enter the movie industry. However, despite their eagerness, they lack experience in movie creation. The challenge lies in understanding the current movie landscape and identifying the types of films that perform well at the box office. This project aims to explore these aspects, and its findings will guide the decision-making process for Microsoft's new movie studio, helping to decide what type of films to create.

## Data

The project leverages several datasets, providing comprehensive movie-related information. Each movie has a unique ID associated with its [intake](link-to-intake-dataset) and [outcome](link-to-outcome-dataset) data. The datasets offer valuable data points, such as movie titles, genres, average ratings, domestic and foreign gross revenues, and release years.

Given the business problem, we recognize the need to incorporate additional data to provide more comprehensive insights. This includes information on movie genre, budget and box office revenue, director and cast, runtime, and regional and language specifics. However, our current dataset includes the movie name, release year, and IMDB rating. Future enhancements of this analysis may include these additional data points.

## Methods

This project uses descriptive analysis, including a description of trends over time. This approach offers a useful overview of the factors affecting box office performance and helps identify key success factors.

## Results

Most successful movies fall within the genres of Action, Comedy, and Drama. Furthermore, there is a positive correlation between movie ratings and box office revenue. The analysis also reveals a moderate budget range associated with successful outcomes.

![results_visualization](./images/results_visualization.png)

## Conclusions

This analysis leads to four key recommendations for Microsoft's new movie studio:

- **Focus on popular genres.** Action, Comedy, and Drama have consistently performed well at the box office.
- **Invest in quality.** Higher-rated movies tend to yield better revenues.
- **Adopt a balanced budget strategy.** Successful movies often have moderate budgets.
- **Release strategically.** Timing plays a crucial role in a movie's box office performance. 

### Next Steps

Further analysis could provide additional insights:

- **Identifying top directors and actors.** Understanding who the key players are in the industry can help ensure successful movies.
- **Marketing strategy assessment.** Analyzing successful marketing campaigns can help craft an effective strategy.
- **Viewer preference prediction.** Predicting viewer preferences could help in creating content that resonates with the audience.

## For More Information

See the full analysis in the [Jupyter Notebook](./movie-analysis-notebook.ipynb) or review this [presentation](./Movie_Analysis_Presentation.pdf).

For additional info, contact Your Name at [Oscar Mulei](mailto:omulei@gmail.com)

![logo](./images/logo.jpg)

## Repository Structure

```
├── data
├── images
├── README.md
├── Movie_Analysis_Presentation.pdf
└── movie-analysis-notebook.ipynb
```
---
