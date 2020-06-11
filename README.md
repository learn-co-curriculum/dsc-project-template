# Module 1 Project Template - Minimum Viable Product (MVP)

![bluebrint2](images/blueprint.png)

This repository is like a blueprint, providing structure for your first data science project. This will allow you to focus less on formatting and organization, and more on the _analysis and communication skills_ that will support your progress through the course.

The template provided here is designed to help support your group collaboration and make your projects portfolio-ready. Employers will often review your GitHub projects, sometimes _before_ an interview, to judge the quality of your work. To set you up for success, we ask you to model your Module 1 project off of this repository. Your repositories for future projects will build on this foundation as you proceed through the course.

## Repository Contents

- TEMPLATE_README: An example of a Readme for your project
  - This should be an brief overview of your whole project
- `dsc-mod1-project-template.ipynb`: A starter Jupyter Notebook
  - Inside the notebook, there is some text and `| guiding questions within lined sections |` that you should answer in narrative form
  - Includes sample visualizations - the code to create them is in the `visualizations.py` file
- `__init__.py`: Python helper file that tells Python that there are packages in the repository that can be imported
- `SampleProjectSlides.PDF`: A starter slide deck
  - PDF of a sample slide deck to use for a presentation to your class or an employer
  - Here is an [online editable version](https://docs.google.com/presentation/d/1PnqhxdN1P1tY3MKCXKmShO0sYLRQF2DSMzMN_tnk5xo/edit?usp=sharing) of the presentation - instructions for using this are below.
- images folder:
  - Contains images referenced in Jupyter Notebook markdown cells
- `.gitignore` file that tells git to not track certain files and folders

***
## Instructions for How to Start

**If in a group project, have only one team member do steps one through five**

1. Through GitHub, fork this repository to your personal account.
2. In GitHub, click "Settings" on the forked repo.
3. On the Setting page, the first tab is "Options". On that page there  "Repository Name" with a text field, and a button "Rename"
4. Change the name of the forked repo to a _descriptive_ name of your choosing. "Microsoft-Movie-Analysis" is a **better** repo name than "Mod-Project-1." Remember that your employer will read this name to understand what your project is about.
5. If you are part of a group project (if not, proceed to step 6):
   - Go to the "Manage Access" tab within "Settings"
   - Add your project team members as collaborators
   - Share the link to the repository with your teammates

**All students should do the following steps**

6. Through the terminal on your local machine, `git clone` the project to your local computer
7. Move the data from the project description into the `data` folder on your local machine
8. You are now ready to start using these materials!

**To use the slide template**

1. Go to [this link](https://docs.google.com/presentation/d/1eYnFN5ojOD7RNXDv9dj-ZBwrASru0pnlnwTg3NVXdoU/edit?usp=sharing) - it will appear as "View Only."
2. Go to "File," select "Make a Copy," and give it a descriptive name - Google will then create an **editable** copy of the slide deck in your own account.
3. If you are part of a group project, click the "Share" button and add your teammates as editors.
4. Go to "Slide," select "Change Theme," and pick a theme you like so your presentation doesn't look like everyone else's.

***
## Instructions for How to Finish
1. Change the file name of the Jupyter Notebook (`dsc-mod1-project-template.ipynb`) to something more descriptive.
2. Delete `SampleProjectSlides.PDF` and save an appropriately-named PDF version of your Google Slides to the repository.
3. Delete **this** readme from the repo using `git rm README.md`, followed by `git mv TEMPLATE_README.md README.md`.

***
## Please note
- The visualizations in the notebook use best practices for visualization that you should try to emulate. For example, they have clear axes, descriptive titles, and appropriate number formatting.
- The `dsc-mod1-project-template.ipynb` is intended to be the _final version_ of your project. The first notebook you create will not look like this. You are encouraged to start with a very disorderly notebook and clean it as you go.
