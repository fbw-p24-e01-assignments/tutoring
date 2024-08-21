## Django Project Setup

#### Set up your project

1. Create a folder for your project and open it in VSCode

```sh {"id":"01J5TWKZ3HX9PWA0JFWY9GBQ3M"}
mkdir project
code project
```

2. Setup a virtual environment and activate it

```sh {"id":"01J5TWMG458J42PC8Q3XS32NH2"}
python3 -m venv env_name
source env_name/bin/activate
```

3. Install Django

```sh {"id":"01J5TWN7RPHQZ27SY9Z4DFMGTB"}
pip install django
```

4. Create a Django project:
    
    if you want to create an outer folder for your project, run

```sh {"id":"01J5TWP4NE81VY0AT2FVVM2X09"}
django-admin startproject project_name
```

otherwise, add a dot at the end (that means that the project folder will be the current folder)

```sh {"id":"01J5TWPZSYW6V3KBPXF8XJZ8JS"}
django-admin startproject project_name .
```


To **see what your site looks like** at any time, make sure you are in the same folder as your `manage.py` file and run

```sh {"id":"01J5TWQGN0NC61FKEQ2FYM5FYS"}
python3 manage.py runserver
```

#### Start coding

Your main setup is done. To start coding your website you need an app with views because views are what will let Django visualise your content. To make an app, run

```sh {"id":"01J5TWQYSMADH01ME5VWB9ADGS"}
django-admin startapp app_name
```

and add it to the installed apps in `project_name/settings.py`, like so

```python {"id":"01J5TWVMZ0VRRSSVF618GPP4BV"}
# project_name/settings.py

INSTALLED_APPS = [
    ...
    'app_name',
]
```

#### Connecting views

When you have coded your first view, you obviously want to see it in the browser, but before you can do that, it needs to be connected to the rest of the project. To do so we work in the `urls.py` files.

Firstly, we create a `urls.py` file in our app folder:

```sh {"id":"01J5TX155HX368WK6CXMMMEJKJ"}
cd app_name
touch urls.py
```

Then we have to link the path to our view in a list called `urlpatterns`. It's important that it's called **urlpatterns** because Django automatically looks for this variable when connecting files and urls.

```python {"id":"01J5TX5EZRDZJH94X6HNE9HC6C"}
# app_name/urls.py

from django.urls import path

urlpatterns = [
    path('', my_view, name='my_view'),
]
```

Notice that the first argument we pass to path is a string.

This is going to be the url path, so if we have a website whose URL is `mywebsite.com` leaving this string empty will make the url of `my_view` `mywebsite.com`.

Instead, if we pass a different value - let's say `abc`, our URL for the same view would become `mywebsite.com/abc`.

Last but not least, we have to connect our `app_name/urls.py` to our `project_name/urls.py`. We can do it by including our whole `app_name/urls.py` to our paths in `project_name/urls.py`:

```python {"id":"01J5TXKQNB0540YWFSA0XMP64A"}
# project_name/urls.py

from django.urls import path, include

urlpatterns = [
    ... ,
    path('', include('app_name.urls'))
]
```

And that's about the connectivity of the files inside a Django project! :)