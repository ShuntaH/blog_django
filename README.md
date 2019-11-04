# Blog
Blog by Django

## Requirements
* Python3.8
* Virtualenv(venv)
* Django2.2
* SQLite3
* Pycharm Professional

## How to setup
````
git clone git@github.com:ShuntaH/blog_django.git

python3.8 -m venv venv
# if python3.8 is not installed yet, you can download it there -> https://www.python.org/

. venv/bin/activate.fish
# if using fish shell

pip install -r requirements.txt

python3.8 manage.py runserver 8002 
````
## PyCharm
Setting

* Language & Framework -> Django

* Mark Enable Django

* Django Project Root -> project

* Settings -> project/project/settings.py

* Manage Script -> project/manage.py

Set Run Configuration

## Library
* Bulma
https://github.com/timonweb/django-bulma
* Flake8(pycodestyle + pyflakes + mccabe)
http://flake8.pycqa.org/en/latest/
---
after installing libraries...
```
$ pip freeze > requirements.txt
```
