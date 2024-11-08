# Playing with the API

``` 
python manage.py shell
```

We’re using this instead of simply typing “python”, because manage.py sets the DJANGO_SETTINGS_MODULE environment variable, which gives Django the Python import path to your mysite/settings.py file.

```
from polls.models import Choice, Question  # Import the model classes we just wrote.
Question.objects.all()
```

Create a new Question

Support for time zones is enabled in the default settings file, so Django expects a datetime with tzinfo for pub_date. Use timezone.now() instead of datetime.datetime.now() and it will do the right thing.
```
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
```

Access model field values via Python attributes.
```
q.question_text
q.pub_date
```

Change values by changing the attributes, then calling save().
```
q.question_text = "What's up?"
q.save()
```

objects.all() displays all the questions in the database.
```
 Question.objects.all()
```

<Question: Question object (1)> isn’t a helpful representation of this object. Let’s fix that by editing the Question model (in the polls/models.py file) and adding a __str__() method to both Question and Choice:
polls/models.py
```
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.


Add a custom method to this model:

polls/models.py
```
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```
Note the addition of import datetime and from django.utils import timezone, to reference Python’s standard datetime module and Django’s time-zone-related utilities in django.utils.timezone, respectively. If you aren’t familiar with time zone handling in Python, you can learn more in the time zone support docs.

Save these changes and start a new Python interactive shell by running python manage.py shell again:
```
quit()
python manage.py shell
from polls.models import Choice, Question
```

Make sure our __str__() addition worked.
```
Question.objects.all()
```

Django provides a rich database lookup API that's entirely driven by keyword arguments.
```
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
```

Get the question that was published this year.
```
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
```

Request an ID that doesn't exist, this will raise an exception.
```
Question.objects.get(id=2)
```

Lookup by a primary key is the most common case, so Django provides a shortcut for primary-key exact lookups.
The following is identical to Question.objects.get(id=1).
```
Question.objects.get(pk=1)
```

Make sure our custom method worked.
```
q = Question.objects.get(pk=1)
q.was_published_recently()
```

Give the Question a couple of Choices. The create call constructs a new Choice object, does the INSERT statement, adds the choice to the set of available choices and returns the new Choice object. Django creates a set to hold the "other side" of a 

ForeignKey relation (e.g. a question's choice) which can be accessed via the API.
```
q = Question.objects.get(pk=1)
```

Display any choices from the related object set -- none so far.
```
q.choice_set.all()
```

Create three choices.
```
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
```

Choice objects have API access to their related Question objects.
```
c.question
```

And vice versa: Question objects get access to Choice objects.
```
q.choice_set.all()
q.choice_set.count()
```

The API automatically follows relationships as far as you need. Use double underscores to separate relationships. This works as many levels deep as you want; there's no limit. Find all Choices for any question whose pub_date is in this year (reusing the 'current_year' variable we created above).
```
Choice.objects.filter(question__pub_date__year=current_year)
```

Let's delete one of the choices. Use delete() for that.
```
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
```

For more information on model relations, see Accessing related objects. For more on how to use double underscores to perform field lookups via the API, see Field lookups. For full details on the database API, see our Database API reference.

&nbsp;

&nbsp;


Sources: https://docs.djangoproject.com/en/3.2/intro/tutorial02/