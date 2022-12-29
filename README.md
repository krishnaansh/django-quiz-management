# django-quiz-management
##  A Django app that makes the use of quiz management and easy to handle!

![PyPI v0.1](https://img.shields.io/badge/PyPI-v0.1-blue.svg)
![MIT License](https://img.shields.io/badge/License-MIT-lightgray.svg)
![Docs](https://img.shields.io/badge/docs-meh-orange.svg)

django-quiz-management is a quiz management to use of create quiz and there question answer and to boost your website.

### Downloading

django-quiz-management is available on The Python Package Index (PyPI). You can simply use ***pip*** to install it:

```bash
$ pip install django-quiz-management
```
### Dependency
We use django nested admin package to make better view and create quiz along with question and answer in django admin

### Installing

1 - Add ```nested_admin``` inside INSTALLED_APPS in settings.py:
2 - Add ```quiz_management``` inside INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
        ...
        'nested_admin',
        'quiz_management',
]
```

3 - Run the migrations:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

And that's it! django-quiz-management should appear in your admin as ```Quiz Managements```.


### Documentation

***[https://github.com/krishnaansh/django-quiz-management/blob/master/docs/README.md](https://github.com/krishnaansh/django-quiz-management/blob/master/docs/README.md)***

### Download

***[https://github.com/krishnaansh/django-quiz-management/releases/download/v1.1/v1.1.zip](https://github.com/krishnaansh/django-quiz-management/releases/download/v1.1/v1.1.zip)***
