# Crowdfunding project

This is the version I created myself from scratch.

This is not the version created in class following Hayley.


## Schema
https://dbdiagram.io/d/5f3b46bf39081a20ae94e5c7

## TO DO

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


-----------------------

# Introduction

(Picture of anita borg)

When I first did a google search about Anita Borg I was a disappointed because she hadn't developed a cool game I could show, nor did she have any cool pictures I could find, like the one Gab showed and did a quiz on.

As I researched more I understood the importance of her work and why she absolutely deserves a spot amongst all the amazing women we got to talk about. Because although she was highly respected as a computer scientist, her biggest mark was as a champion and mentor of women in the tech world. She founded several initiatives for women in tech and became virtually synonymous with involving women in tech.

But to be honest with you guys, even after reading this I wasn't super excited about her until I read about her life and her as a person, and this is what I am going to talk about. Then Teagen is going to talk about her initiatives to get women in the field of tech.


# Life/work

(slide with main points)

She was born in Chicago in 1949, and died of brain cancer in 2003 (she was 54).

As a child, she grew up and traveled with her family all over the US, including a year camping across the country when she was 9 and then Hawaii for a year.

The attitude of her parents about life was always that you should have a good time and they could do anything they wanted, and if it didn't work out, well, what the heck?

She atributes her love of math to her mother: whenever her mother would help Anita with her homework, she approached it with curiosity, like math was a fun puzzles, and there was no sense of fear.

Anita did 2 years of college studying mostly maths, but she quit her studies to support her husband through college.

The first job she got was with Fortran. She did the training part, then over the long weekend she went to Woodstock. When she came back, she was sick for six weeks and lost the job.

The next job was as a clerk a small insurance company. She was about 20 then. She taught herself COBOL and ended up doing programming jobs for them.

About that time she got divorced, and she quit her job and went back to school.

She decided to major in computer science, because she believed maths was not going to give her a way to support herself, but computer science was.

Her plan was to just finish her undergrad. "At that time I was living with a lawyer, and our plan was: we were going to hop in our van with our two big motorcycles, and we were going to move to Oregon. He was going to be a hippie lawyer, and I was going to be a hippie programmer, and we were going to have hippie babies and grow pot in the backyard."

She ended up getting into the graduate program at NYU and finished her PhD in 8 years because she had her dad's attitute about life, which was: she told them really clearly that graduate school was a five-days-a-week, eight-hours-a-day job, and she was going to go have fun on the weekends. She was going to go ride motorcycles, paddle kayaks and all the other stuff that she does. She had a relationship and a life.

Her thesis was about synchronisation mechanisms in operating systems. She went to work for Auragen building a fault-tolerant operating system. This company went burst and Nixdorf took the technology and hired Anita (the only out of her team) to go to Germany for a year to help them finish up the  fault-tolerance part, because that had been her baby.

She got a paper out of this work back when she was still at Auragen and she presented a few times and eventually in California, where she got a job at DEC to work on operating systems but eventually worked on performance analysis of memory systems.

It was while she was a DEC that she created Systers and subsequently her other initiatives for women in tech, and Teagen will talk about these to you.



# Quotes

"I think that it’s important not to pay too much attention to the stereotype that you somehow have to be one of these geeky guys, which is completely ridiculous. Not everybody’s like that; most people aren’t like that. [...] The stereotype is just a stereotype, it’s not reality; and you shouldn’t let that hinder you."




# Alternative quote (not using this one, maybe you want it?)

"It’s not always going to be easy. But if you enjoy it, there’s a whole lot of fun; there’s a whole lot of pleasure. And there are great things to be done. It’s hard, sometimes, to see: the way computing and technology are often taught, we lose the connection with the impact of what we’re creating. It’s a really good idea to think about all the incredible things that could be done with all of this, if you care about that; because sometimes people won’t talk about it, and it’s really important. And if that will carry you through, then hang on to it."
# Introduction

(Picture of anita borg)

When I first did a google search about Anita Borg I was a disappointed because she hadn't developed a cool game I could show, nor did she have any cool pictures I could find, like the one Gab showed and did a quiz on.

As I researched more I understood the importance of her work and why she absolutely deserves a spot amongst all the amazing women we got to talk about. Because although she was highly respected as a computer scientist, her biggest mark was as a champion and mentor of women in the tech world. She founded several initiatives for women in tech and became virtually synonymous with involving women in tech.

But to be honest with you guys, even after reading this I wasn't super excited about her until I read about her life and her as a person, and this is what I am going to talk about. Then Teagen is going to talk about her initiatives to get women in the field of tech.


# Life/work

(slide with main points)

She was born in Chicago in 1949, and died of brain cancer in 2003 (she was 54).

As a child, she grew up and traveled with her family all over the US, including a year camping across the country when she was 9 and then Hawaii for a year.

The attitude of her parents about life was always that you should have a good time and they could do anything they wanted, and if it didn't work out, well, what the heck?

She atributes her love of math to her mother: whenever her mother would help Anita with her homework, she approached it with curiosity, like math was a fun puzzles, and there was no sense of fear.

Anita did 2 years of college studying mostly maths, but she quit her studies to support her husband through college.

The first job she got was with Fortran. She did the training part, then over the long weekend she went to Woodstock. When she came back, she was sick for six weeks and lost the job.

The next job was as a clerk a small insurance company. She was about 20 then. She taught herself COBOL and ended up doing programming jobs for them.

About that time she got divorced, and she quit her job and went back to school.

She decided to major in computer science, because she believed maths was not going to give her a way to support herself, but computer science was.

Her plan was to just finish her undergrad. "At that time I was living with a lawyer, and our plan was: we were going to hop in our van with our two big motorcycles, and we were going to move to Oregon. He was going to be a hippie lawyer, and I was going to be a hippie programmer, and we were going to have hippie babies and grow pot in the backyard."

She ended up getting into the graduate program at NYU and finished her PhD in 8 years because she had her dad's attitute about life, which was: she told them really clearly that graduate school was a five-days-a-week, eight-hours-a-day job, and she was going to go have fun on the weekends. She was going to go ride motorcycles, paddle kayaks and all the other stuff that she does. She had a relationship and a life.

Her thesis was about synchronisation mechanisms in operating systems. She went to work for Auragen building a fault-tolerant operating system. This company went burst and Nixdorf took the technology and hired Anita (the only out of her team) to go to Germany for a year to help them finish up the  fault-tolerance part, because that had been her baby.

She got a paper out of this work back when she was still at Auragen and she presented a few times and eventually in California, where she got a job at DEC to work on operating systems but eventually worked on performance analysis of memory systems.

It was while she was a DEC that she created Systers and subsequently her other initiatives for women in tech, and Teagen will talk about these to you.



# Quotes

"I think that it’s important not to pay too much attention to the stereotype that you somehow have to be one of these geeky guys, which is completely ridiculous. Not everybody’s like that; most people aren’t like that. [...] The stereotype is just a stereotype, it’s not reality; and you shouldn’t let that hinder you."




# Alternative quote (not using this one, maybe you want it?)

"It’s not always going to be easy. But if you enjoy it, there’s a whole lot of fun; there’s a whole lot of pleasure. And there are great things to be done. It’s hard, sometimes, to see: the way computing and technology are often taught, we lose the connection with the impact of what we’re creating. It’s a really good idea to think about all the incredible things that could be done with all of this, if you care about that; because sometimes people won’t talk about it, and it’s really important. And if that will carry you through, then hang on to it."

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






