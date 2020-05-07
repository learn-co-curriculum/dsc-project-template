# Module 1 project template - Above and Beyond

![bluebrint2](images/blueprint.png)

A blueprint provides guidance and structure before something in created. This repoistory provides similar sturcture and guidance for your first data science project. How analysis is structured is will provide the foundation for your work. This guidance also alllows to students to focus on the _foundational skills_ what will be built upon lter in the course.

Student repositories are  useful in the job search, as employers can see the qualitiy of student work _before_ the interview. To set students up for success, the module 1 project is expected to mirror the structure of this repository. All content is in draft form, to guide students in creating project repositories. Repository structure will mature further with later projects.

This repo contains:
- TEMPLATE_README: An example of a Readme for your project 
  - This should be an abstract of your complete analysis
- `dsc-mod1-project-template.ipynb`: A starter jupyter notebook
  - inside the notebook there is some text and `| guiding questions within lined sections |` that should be answered in narrative form
  - sample visualizations. Their code is in the `visualizations.py` file as a reference. 
- `__init__.py` :python helper file, tells python there are packages 
- presentation pdf:
  - PDF of slide deck used in class presentation, [online version also provided](https://docs.google.com/presentation/d/1PnqhxdN1P1tY3MKCXKmShO0sYLRQF2DSMzMN_tnk5xo/edit?usp=sharing) in readme.
  - The online editable version of this file can be found [here](https://docs.google.com/presentation/d/1iS5kCJVBiieuUEokWLOSjuAxlz9oX-tPV2xr0i9RYdA/edit?usp=sharing)
  - Please make a copy of the file before editing
- code folder:
  - `__init__.py` :python helper file, tells python there are packages 
  - contains sample `data_cleaning.py` script to clean data and prepare it for analysis and visualization
  - contains sample `visualizations.py` to produce visualizations
  - You may find it helpful to have a notebook here for messy EDA or data preparation
- images folder:
  - contains images used in jupyter notebook markdown
- hidden `.gitignore` file that tells git to not track certain files and folders

***
## Student instructions

1. Through github, fork this repository to you own account 

**If in a group project, have only one team member do steps one through five**

2. In github, on the forked repo, click "Settings"
3. On the Setting page, the first tab is "Options". On that page there  "Repository Name" with a text field, and a button "Rename"
4. Change the name of the forked repo to a _decriptive_ project repo name of your choosing. "Microsoft-Movie-Analsis" is a **better** repo name than "Mod-Project-1"
5. If you are part of a group project(if not, proceed to step 6):
   - Go to the "Manage Access" tab within "settings"
   - Add your project team members as collaborators
   - copy the link to clone the repository and share it with teammates 


6. Through the terminal on your local machine, `git clone` the project to your local computer
7. Move the data from the project description into the `data` folder on your local machine
8. You are now ready to start using these materials!

**To use the slide template**
1. Go to [this link](https://docs.google.com/presentation/d/1eYnFN5ojOD7RNXDv9dj-ZBwrASru0pnlnwTg3NVXdoU/edit?usp=sharing)
2. The google slides will show that they are "view only"
3. Go to "File" and select "Make a Copy"
4. Google will then create an **editable** copy of the slide deck in your own account.

***
## Please note
- The code within `visualizations.py` and `data_cleaning.py` is an example of well documented code.
- The visualizations in the notebook, generated from `visualizations.py` have clear axes, titles, and appropriate number formatting. Please use as a reference.
- The `dsc-mod1-project-template.ipynb`is intented to be the _final version_ of your project. 
     - The first noteook you create will not look like this. 
     - You are encouraged to start with a very disorderly notebook and clean it as you go.
- Before you finish this project, delete **this** readme from the repo using `git rm README.md`, followed by `git mv TEMPLATE_README.md README.md`
