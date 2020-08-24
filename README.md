# Phase 1 Project Template - Minimum Viable Product (MVP)

![bluebrint2](images/blueprint.png)

This repository is like a blueprint, providing structure for your first major data science project. This will allow you to focus less on formatting and organization, and more on the _analysis and communication skills_ that will support your progress through the course.

The template provided here is designed to help make your projects portfolio-ready. Employers will often review your GitHub projects, sometimes _before_ an interview, to judge the quality of your work. To set you up for success, we ask you to model your Phase 1 project off of this repository. Your repositories for future projects will build on this foundation as you proceed through the course.

## Repository Contents

- `README.md`: The README for this repo branch explaining it's contents - you're reading it now
- `TEMPLATE_README.md`: An example of a README for your project
  - This is a brief overview of your whole project
- `dsc-phase1-project-template.ipynb`: A starter Jupyter Notebook
  - Inside the notebook, there is some text and guiding questions that you should answer in narrative form
- `DS_Project_Presentation_Template.pdf`: A starter slide deck
  - Here is an [online editable version](https://docs.google.com/presentation/d/1PaiH1bleXnhiPjTPsAXQSiAK0nkaRlseQIr_Yb-0mz0/copy) of the presentation
- `data` folder:
  - Contains data referenced in Jupyter Notebook code cells
- `images` folder:
  - Contains images referenced in other files
- `.gitignore` file that tells git to not track certain files and folders

## Instructions

### Forking This Repository

**For a group project**, have only one team member do these steps:

1. Fork this repository to your personal account
   - In GitHub, go to this repository and click the "Fork" button in the upper right
   
2. Change the name of the forked repo to a _descriptive_ name of your choosing
   - In GitHub, go to the forked repo -> "Settings" -> "Options" -> "Repository Name" -> "Rename"
   - Potential employers will read this name to learn about your project, so make it descriptive. Ex: "Microsoft-Movie-Analysis" is better than "Project-1"

3. Use `git clone` to clone both the Phase 1 Project repo and your fork of this repo to your local computer

4. Copy the data from the Phase 1 Project repo into the `data` folder for your fork of this repo

5. **For a group project**, add team members as collaborators to the forked repo:
   - In GitHub, go to the forked repo -> "Settings" -> "Manage Access" -> "Invite Teams or People"
   - Add your project team members as collaborators & share the link to the repository

### Working In Your Forked Repo

- Work in the clone of the forked repo that lives on your local machine, and commit your work to GitHub often
- Start writing and coding in the Jupyter Notebook `dsc-phase1-project-template.ipynb`
- Fill in the README template in `TEMPLATE_README.md`

### Using The Slide Template

1. Go to [this link](https://docs.google.com/presentation/d/1PaiH1bleXnhiPjTPsAXQSiAK0nkaRlseQIr_Yb-0mz0/copy) to make an editable copy of the slide deck in your own Google Drive account
2. Go to "Slide," select "Change Theme," and pick a theme you like so your presentation doesn't look like everyone else's
3. **For a group project**, click the "Share" button and add your teammates as editors

### Cleaning Up Your Project

1. Change the file name of the Jupyter Notebook (`dsc-phase1-project-template.ipynb`) to something more descriptive

2. Save an appropriately-named PDF version of your slide deck to the repository

3. Delete unnecessary files from the repo using `git rm`
  - The presentation PDF: `DS_Project_Presentation_Template.pdf`
  - This README file: `README.md`
  - Any unused images in the `images` folder
  
4. Rename the template readme you've been working in by running `git mv TEMPLATE_README.md README.md`

### Submitting Your Project

To submit your project, please follow the instructions in the "Project Requirements & Submission" page in the Milestones course.

***
### Notes

- The visualizations in the notebook use best practices for visualization that you should try to emulate. For example, they have clear axes, descriptive titles, and appropriate number formatting.
- The `dsc-phase1-project-template.ipynb` is intended to be the _final version_ of your project. The first notebook you create will not look like this. You are encouraged to start with a very disorderly notebook and clean it as you go.
