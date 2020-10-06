# Crowdfunding project

This is the version I created myself from scratch.

This is not the version created in class following Hayley.


## Schema
https://dbdiagram.io/d/5f3b46bf39081a20ae94e5c7

## TO DO

- Need way to modify project, especially to publish.

- in /users/, for post (create user), want there to be 2 passwords
Apparently this is done in the front end
https://stackoverflow.com/questions/43031323/how-to-create-a-new-user-with-django-rest-framework-and-custom-user-model


- Private messages

- Notifications


- do I need to limit the number of projects I send in the categories
  view (because I will only want to show maybe 4 for each category) or
  is this a front end's problem?

- users profile, user can see their own pledges (or can anybody see
them?)

- can people see a person's projects?





1. Create new profile
- handle registration of new users
- validate profile data

2. Listing existing profiles
- search for profiles
- email and name

3. View specific profiles
- profile id

4. Update profile of logged in user
- change name, email and password

5. Delete profile





## Helpful links

https://stackoverflow.com/questions/51920166/django-rest-framework-single-class-based-view-bound-to-multiple-urls


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

$ git push heroku master

### Apps

added to settings.py

    'rest_framework',
    'projects.apps.ProjectsConfig', 
    'users.apps.UsersConfig',


Added projects, categories, users models

### Create superuser

python3 manage.py creesuperuser

### Register projects and categories in admin

admin.site.register(Project)
admin.site.register(Category)



### SHELL

>>> from projects.serialisers import ProjectSerialiser
>>> serialiser = ProjectSerialiser()
>>> print(repr(serialiser))
ProjectSerialiser():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=200)
    description = CharField(style={'base_template': 'textarea.html'})
    goal = IntegerField()
    image = URLField(max_length=200)
    is_open = BooleanField()
    date_created = DateTimeField()
    pub_date = DateTimeField(allow_null=True, required=False)
    owner = PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    category = PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)
>>> 

---------------------------------------------------------------------

>>> from projects.models import Project
>>> from projects.serialisers import CategorySerialiser
>>> from projects.models import Category
>>> obj = Category.objects.filter(id=1)
>>> print(obj)
<QuerySet [<Category: Other>]>
>>> obj = Category.objects.get(id=1)
>>> obj.id
1
>>> obj.name
'Other'
>>> data = {
...     "name": "delete",
...     "description": "testing the shell"
... }
>>> new_item = CategorySerialiser(data = data)
>>> new_item
CategorySerialiser(data={'name': 'delete', 'description': 'testing the shell'}):
    id = IntegerField(label='ID', read_only=True)
    cat_projects = ProjectSerialiser(many=True, read_only=True):
        id = IntegerField(label='ID', read_only=True)
        owner = ReadOnlyField(source='owner.username')
        date_created = ReadOnlyField()
        title = CharField(max_length=200)
        description = CharField(style={'base_template': 'textarea.html'})
        goal = IntegerField()
        image = URLField(max_length=200)
        is_open = BooleanField()
        pub_date = DateTimeField(allow_null=True, required=False)
        category = PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)
    name = CharField(max_length=15, validators=[<UniqueValidator(queryset=Category.objects.all())>])
    description = CharField(style={'base_template': 'textarea.html'})
>>> 


--------------------------------------------------

>>> from projects.models import Category
>>> from projects.serialisers import CategorySerialiser
>>> data = {
...     "name": "delete",
...     "description": "testing the shell"
... }
>>> new_item = CategorySerialiser(data=data)
>>> new_item
CategorySerialiser(data={'name': 'delete', 'description': 'testing the shell'}):
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=15, validators=[<UniqueValidator(queryset=Category.objects.all())>])
    description = CharField(style={'base_template': 'textarea.html'})
>>> new_item.initial_data
{'name': 'delete', 'description': 'testing the shell'}
>>> if new_item.is_valid():
...     new_item.save()
... else:
...     print(new_item.errors)
... 
<Category: delete>
>>> new_item.data
{'id': 5, 'name': 'delete', 'description': 'testing the shell'}


--------------------------------------
### Adding favourites

from projects.models import Favourite
from projects.models import Project
from users.models import CustomUser

Favourite.objects.create(owner=CustomUser.objects.get(id=1),project=Project.objects.get(id=2))


proj = Project.objects.get(id=2)
proj.favouriters.all()




"""
data = {
    "name": "delete",
    "description": "testing the shell"
}

new_item = CategorySerialiser(data=data)

if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""

-----------------------------






