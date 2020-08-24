# Crowdfunding project

This is the version I created myself from scratch.

This is not the version created in class following Hayley.



## STEPS

### Virtual Environment

- Add a requirements.txt file.
- Create a virtual environment.
$ virtualenv venv
- Activate the virtual environment on Unix based:
$ . venv/bin/activate
- Install the requirements:
$ pip3 install -r requirements.txt


### Django Project

$ django-admin startproject crowdfunding
$ cd crowdfunding
$ python3 manage.py startapp projects

### Django Users

$ python3 manage.py startapp users


### Git

- Created the .gitignore file
Then

$ git init .
$ git add .

$ git commit -am "Configured Vagrant and setup hello world script"

Then went on github desktop and added repository (add from existing) and published it

From now on can use :

$ git push origin


### Apps

added to settings.py

    'rest_framework',
    'projects.apps.ProjectsConfig', 
    'users.apps.UsersConfig',


Added projects, categories, users models

### Create superuser

python3 manage.py creesuperuser
