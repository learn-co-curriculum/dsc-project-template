#  MICROSOFT MOVIE STUDIO MARKET RESEARCH
## Author:Winfred Kabuya

![image](images/Microsoft movie studio.jpeg)

 ## Overview
This project aims to provide recommendations to Microsoft regarding the types of movies that perform well among audiences, using data analysis of movie ratings and popularity. Microsoft plans to launch its own movie studio and has requested guidance as a newcomer to the industry. The project utilizes datasets from various sources, such as Box Office Mojo, IMDb, Rotten Tomatoes, The Movie Database, and The Numbers. The primary focus of the analysis is the IMDb datasets, which include movie information from 2010 to 2019, such as genres, average user ratings, and the number of users who voted on each movie. The analysis resulted in identifying 10 high-performing genres for Microsoft to prioritize and providing recommendations on how much of its budget should be allocated to Action movies and animated movies.

## Business Problem
When measuring success in the movie industry, it may not be sufficient to only consider the attributes that generate the highest return-on-investment at the box office, especially in the streaming era. Rather, the number of people who watch the movie should be the primary measure of success. As Microsoft considers whether to sell its movies to streaming services or launch its own, it needs to determine which types of movies will attract the most viewers. To gauge this, I use the number of votes a movie receives on IMDb as a proxy for the number of viewers. By analyzing this metric, I aim to answer the following questions: which 5 genres typically perform the best, and how much focus should Microsoft place on producing comedies and action movies? 

## Data Understanding

IMDb is a highly popular website for obtaining basic information on movies and TV shows, including user reviews.As of March 2022, the database contained some 10.1 million titles (including television episodes) and 11.5 million person records. Additionally, the site had 83 million registered users and is the 54th most visited website in the world, according to website ranker Alexa as of February 12, 2023.

The data that I will be working with is stored in a SQL file and contains two main tables: movie_basics and movie_ratings. The movie_basics table provides details on each movie's name, release year, runtime, and genres, while the movie_ratings table presents the total number of votes a movie has received and its rank based on those votes.

Both tables share a unique identifier for each movie called movie_id. To analyze the data, I intend to group the movies by genre and determine the number one ranked movie for each genre based on its total number of votes.

## Repository Contents

Below is a list of the contents of this repository - instructions for using them are in the next section.

- `README.md`: The README for this repo branch explaining it's contents - you're reading it now
- `TEMPLATE_README.md`: An example of a project README that provides a brief overview of your whole project
- `dsc-phase1-project-template.ipynb`: A starter Jupyter Notebook with headings, code examples and guiding questions
- `DS_Project_Presentation_Template.pdf`: A starter slide deck presenting your project - here is an [editable version](https://docs.google.com/presentation/d/1PaiH1bleXnhiPjTPsAXQSiAK0nkaRlseQIr_Yb-0mz0/copy)
- `zippedData` folder: A folder for the data you reference with your code
- `images` folder: A folder for the images you reference in your files 
- `.gitignore`: A hidden file that tells git to not track certain files and folders

## Instructions For Using This Repository

### Fork This Repository

**For a group project**, have only one team member do these steps:

1. Fork this repository to your personal account
   - In GitHub, go to this repository and click the "Fork" button in the upper right
   
2. Change the name of your fork of this repo to a _descriptive_ name of your choosing
   - In GitHub, go to your fork of this repo -> "Settings" -> "Options" -> "Repository Name" -> "Rename"
   - Make the name descriptive, since potential employers will read it. Ex: "Microsoft-Movie-Analysis" is better than "Project-1"

3. Use `git clone` to clone your fork of this repo to your local computer

4. **For a group project**, add team members as collaborators to your fork of this repo
   - In GitHub, go to your fork of this repo -> "Settings" -> "Manage Access" -> "Invite Teams or People"
   - Add your project team members as collaborators & send them the repo GitHub URL

### Work In Your Fork Of This Repository

- Work in the repo clone that you created on your local machine
- Start writing and coding in the Jupyter Notebook `dsc-phase1-project-template.ipynb`
- Fill in the README template in `TEMPLATE_README.md`
- Use `git add`, `git commit`, and `git push` often to update your repo in GitHub
   - For a refresher on how to do this and why it's important, review Topic 2: Bash and Git

### Use The Slide Template

1. Go to [this link](https://docs.google.com/presentation/d/1PaiH1bleXnhiPjTPsAXQSiAK0nkaRlseQIr_Yb-0mz0/copy) to make an editable copy of the slide deck in your own Google Drive account
2. Go to "Slide," select "Change Theme," and pick a theme you like so your presentation doesn't look like everyone else's
3. **For a group project**, click the "Share" button and add your teammates as editors

### Tidy Up Your Project

- Change the file name of the Jupyter Notebook (`dsc-phase1-project-template.ipynb`) to something more descriptive
- Save an appropriately-named PDF version of your slide deck to the repository
- Rename the template readme you've been working in by running `git mv TEMPLATE_README.md README.md`
- Delete unnecessary files from the repo using `git rm`
   - The presentation PDF: `DS_Project_Presentation_Template.pdf`
   - Any unused data files in the `zippedData` folder
   - Any unused images in the `images` folder
- Utilize the .gitignore file to ignore large unzipped data files in the `zippedData` folder
   - Add `*.csv`,`*.tsv`, and `*.db` to the .gitignore file

### Submit Your Project

To submit your project, please follow the instructions in the "Project Submission & Review" page in the Milestones course.

***
### Notes

- The visualizations in the notebook use best practices for visualization that you should try to emulate. For example, they have clear axes, descriptive titles, and appropriate number formatting
- The `dsc-phase1-project-template.ipynb` is intended to be the _final version_ of your project. The first notebook you create will not look like this. You are encouraged to start with a very disorderly notebook and clean it as you go
