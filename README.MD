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

Then followed the instructions in "Crowdfunding Users.pdf" plus part of the admin.py  changes from SheCodesNews
