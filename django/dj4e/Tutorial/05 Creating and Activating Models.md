# Creating models
polls/models.py
```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

- Each model is represented by a class that subclasses django.db.models.Model. 
- Each model has a number of class variables, each of which represents a database field in the model.
- Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. 
- The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.
- You can use an optional first positional argument to a Field to designate a human-readable name. If this field isn’t provided, Django will use the machine-readable name. In this example, we’ve only defined a human-readable name for Question.pub_date. For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.
- A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.
- A relationship is defined using ForeignKey. That tells Django each Choice is related to a single Question. 

&nbsp;


# Activating models
That small bit of model code gives Django a lot of information. With it, Django is able to:

- Create a database schema (CREATE TABLE statements) for this app.
- Create a Python database-access API for accessing Question and Choice objects.

But first we need to tell our project that the polls app is installed.

Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps.

To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. 

mysite/settings.py 
```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
By running makemigrations, you’re telling Django that you’ve made some changes to your models and that you’d like the changes to be stored as a migration.
```
python manage.py makemigrations polls
```

- Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py. 

The sqlmigrate command takes migration names and returns their SQL:
```
python manage.py sqlmigrate polls 0001
```

Note the following:

- The exact output will vary depending on the database you are using. 
- Primary keys (IDs) are added automatically. 
- By convention, Django appends "_id" to the foreign key field name.
- The foreign key relationship is made explicit by a FOREIGN KEY constraint. Don’t worry about the DEFERRABLE parts; it’s telling PostgreSQL to not enforce the foreign key until the end of the transaction.
- The sqlmigrate command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required.
- If you’re interested, you can also run python manage.py check; this checks for any problems in your project without making migrations or touching the database.

Now, run migrate again to create those model tables in your database:
```
python manage.py migrate
```

- The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

The three-step guide to making model changes:

1 Change your models (in models.py).

2 Run python manage.py makemigrations to create migrations for those changes

3 Run python manage.py migrate to apply those changes to the database.


&nbsp;

&nbsp;


Sources: https://docs.djangoproject.com/en/3.2/intro/tutorial02/