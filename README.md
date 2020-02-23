<<<<<<< HEAD
# Tiki Web scrawling
## Introduction
*In this project we try to scrawl all categories of tiki website,save them in our own database and reload later*

## Project structure
templates templates/index.html templates/table.html
app.py
display.py
lyst_category.py
query.sql

## Process
### Find all categories
*There maybe a wide range of categories. Some are main categorie,which means they don't have parent at all.Some are minimum sub categorie,which means no children belongs to them.The rest have both children and parents.Our task in this section is find all possible parent categories.Code is available in `lyst_category.py`.You guys can type `python lyst_category.py` to execute this mission*

### Scrawl all products of all categories
*After we have full kind of categories.Now we can use beautiful soup library to scrawl.Code is available in `app.py`.You guys just type `python app.py` to execute this task.Note that you guys need to change to your own database!*

### Display all products in table form
*After scrawling successfully,you guys can display in table form or card form.`display.py` contains the function help you guys reload from your own databse(remember changing this as well !).You guys can choose the display form by chosing render to `table.html`(limit 50 products) or `index.html` (limit 10 products)*

