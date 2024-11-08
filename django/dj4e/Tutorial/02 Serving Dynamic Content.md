# Adding Your Polls Application

```
cd ~/django_projects/mysite
python3 manage.py startapp polls
```
&nbsp;


# Write your first view
Open the file polls/views.py and put the following Python code in it:
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
To create a URLconf in the polls directory, create a file polls/urls.py. Your app directory should now look like:


In the polls/urls.py file include the following code:
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
In mysite/urls.py paste
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

```
&nbsp;


# Running the server
python3 manage.py runserver     # <-- Never run this on pythonanywhere

```
cd ~/django_projects/mysite
python3 manage.py check
```
The check does a check for syntax and logic errors in your Django application. It is easier to fix errors in the command line.

Navigate to the Web tab in Python anywhere and Reload your application and then test your application by navigating to:

(your-account).pythonanywhere.com/polls

You should see a line that looks like:

Hello, world. You're at the polls index.

Going forward, every time we make changes to our application, we should run

```
python3 manage.py check
```
&nbsp;


# Starting Over Fresh

If you have followed instructions and it just does not work and you want to start over at the beginning of this assignment, here are the steps to clear things out:

Remove all of your running consoles under the www.pythonanywhere.com Consoles tab

Open a new bash console from the Consoles tab. Do not run the workon command and run the following commands:

    cd ~
    rm -rf .virtualenvs/django3
    rm -rf dj4e-samples
    rm -rf django_projects

&nbsp;

&nbsp;

Sources:

https://www.dj4e.com/assn/dj4e_install.md

https://docs.djangoproject.com/en/3.0/intro/tutorial01/