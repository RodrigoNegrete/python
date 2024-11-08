# Setting Up Your Environment

Once you have created your PYAW account, start a bash shell and set up a virtual environment with Python 3.x and Django 3.
```
mkvirtualenv django3 --python=/usr/bin/python3.6
pip install django ## this may take a couple of minutes
workon django3
python -m django --version

```
&nbsp;


# Installing the Sample Code for DJ4E
```
cd ~
git clone https://github.com/csev/dj4e-samples
cd dj4e-samples
pip install -r requirements.txt
python3 manage.py check
python3 manage.py makemigrations
```
This is the normal output of the makemigrations:

When you want to use social login, please see dj4e-samples/github_settings-dist.py
Using registration/login.html as the login template
No changes detected

Then run:
```
python3 manage.py migrate
```
&nbsp;


# Build your first application in the PYAW shell:
```
cd ~
mkdir django_projects
cd django_projects
django-admin startproject mysite
nano ~/django_projects/mysite/mysite/settings.py
```
Change the allowed hosts line (around line 28) to be:
```
 ALLOWED_HOSTS = [ '*' ]
```
Save the File by pressing 'CTRL-X', 'Y', and Enter
&nbsp;


# Running Your Application
In the PYAW web interface navigate to the Web tab to create a new web application. You do not need to upgrade your account - they give you one application like drchuck.pythonanywhere.com - use this free application for the course.

When making the new application, do not create a "Django application" - instead, select manual configuration and Python 3.6. Once the webapp is created, you need to make a few changes to the settings for the web app and your application.

- Source code: /home/drchuck/django_projects/mysite

- Working directory: /home/drchuck/django_projects/mysite

- Virtualenv: /home/drchuck/.virtualenvs/django3

Replace drchuck with your account on PythonAnywhere.

Delete the existing content of the WGSI Configuration File file and completely replace it with the text below. 

```
import os
import sys

path = os.path.expanduser('~/django_projects/mysite')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
```

Once the above configuration is complete, go back to the top of the PYAW Web tab, Reload your web application, wait a few seconds and check that it is up and running:

http://(your-account).pythonanywhere.com/
&nbsp;

&nbsp;

Sources: https://www.dj4e.com/assn/dj4e_install.md
