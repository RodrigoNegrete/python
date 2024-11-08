# Adding HTML Content to Django
&nbsp;

## Serving HTML Content
```
mkdir ~/django_projects/mysite/site
mkdir ~/django_projects/mysite/site/subfolder
```

Create a file at ~/django_projects/mysite/site/hello.txt with the text "Hello World".

Create a file at ~/django_projects/mysite/site/subfolder/hello.html with this text: 
```
<h1>Hello World</h1>
```

Change your ~/django_projects/mysite/mysite/urls.py to be:
```
import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve


# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),                                                                                           
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
]
```

Check for errors using:
```
cd ~/django_projects/mysite
python3 manage.py check
```
Go to the Web tab on PythonAnywhere, reload your application and then check your application by navigating to:

(your-account).pythonanywhere.com

&nbsp;


## Viewing Your New Files
Go to (your-account).pythonanywhere.com/site -

&nbsp;


## Building Some Validated HTML
Create a web page in a file named dj4e.htm and store it in the site folder
```
<!DOCTYPE html>
<html>
    <head>
        <title>Rodrigo Instructor 4c56ff</title>
        <meta charset="UTF-8">
    </head>
    <body>
        ...
    </body>
</html>
```

Your HTML must pass the validator at:

https://validator.w3.org/nu/

&nbsp;

&nbsp;

Sources: https://www.dj4e.com/assn/dj4e_html.md