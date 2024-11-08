# Database setup

Open up mysite/settings.py. 

By default, the configuration uses SQLite.

If you wish to use another database, install the appropriate database bindings and change the following keys in the DATABASES 'default' item to match your database connection settings:

Bindings: https://docs.djangoproject.com/en/3.2/topics/install/#database-installation

- ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'. Other backends are also available.
- NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, BASE_DIR / 'db.sqlite3', will store the file in your project directory.

If you are not using SQLite as your database, additional settings such as USER, PASSWORD, and HOST must be added. For more details, see the reference documentation for DATABASES.

&nbsp;


## For databases other than SQLite

If you’re using a database besides SQLite, make sure you’ve created a database by this point. Do that with “CREATE DATABASE database_name;” within your database’s interactive prompt.

Also make sure that the database user provided in mysite/settings.py has “create database” privileges. 

&nbsp;


## Editing mysite/settings.py
set TIME_ZONE to your time zone.

Note the INSTALLED_APPS setting at the top of the file. 

By default, INSTALLED_APPS contains the following apps, all of which come with Django:

- django.contrib.admin – The admin site. You’ll use it shortly.
- django.contrib.auth – An authentication system.
-django.contrib.contenttypes – A framework for content types.
- django.contrib.sessions – A session framework.
- django.contrib.messages – A messaging framework.
- django.contrib.staticfiles – A framework for managing static files.

These applications are included by default as a convenience for the common case.

&nbsp;


## Create database tables
```
python manage.py migrate
```
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). 

&nbsp;


## For the minimalists
The default applications are included for the common case, but not everybody needs them. If you don’t need any or all of them, feel free to comment-out or delete the appropriate line(s) from INSTALLED_APPS before running migrate. The migrate command will only run migrations for apps in INSTALLED_APPS.

&nbsp;

&nbsp;


Sources: https://docs.djangoproject.com/en/3.2/intro/tutorial02/