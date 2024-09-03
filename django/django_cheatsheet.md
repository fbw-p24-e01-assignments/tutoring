## Django Cheatsheet

#### When and where to use the Django files

##### `project/settings.py`

| situation | what to do | description |
| --- | --- | --- |
| **apps** | ![app registration](images/apps.png) | After creating an app with `django-admin startapp`, you need to register it as in the `INSTALLED_APP` list |
| **databases** | ![database registration](images/db.png) | To connect to a database, you have to register its engine (`postgres_psycopg2`), name (`my_db`), user to be accessed as, password of the user, host (`'127.0.0.1'` for localhost) and port (optional, `'5432'` for postgres) in the `default` dictionary of the `DATABASES` variable |
| **static files** | ![static file dir registration](images/static.png) | If your static folder is outside of your app, you need to register the folder by adding the variable `STATICFILES_DIRS`, which is going to be a list containing a string path to the folder |
| **templates** | ![templates registration](images/templates.png) | If you want to use templates, you have to register them in the `'DIRS'` key of the `TEMPLATES` variable as a path to the folder |

##### `project/urls.py`

| situation | what to do | description |
| --- | --- | --- |
| **add urls from class-based views** | ![class-based view url registration](images/proj_class_url.png) | Register a new url that shows a class-based view by passing the new url, the class-based view (imported from `app.views`) modified by the `.as_view()` method and a name that identifies the view (optional) |
| **add urls from function-based views** | ![func-based view url registration](images/proj_func_url.png) | Register a new url that shows a function-based view by passing the new url, the function-based view (imported from `app.views`) and a name that identifies the view (optional) |
| **include urls** from apps | ![url registration](images/proj_url.png) | Use the `include` function (imported from `django.urls`) to connect to other files that include urls |

#### `app/urls.py`

NB: This file is not created by default so you have to create it yourself when you make an app. You will also have to write in the `urlpatterns` list variable.

| situation | what to do | description |
| --- | --- | --- |
| **add urls from class-based views** | ![class-based view url registration](images/url-from-class.png) | Register a new url that shows a class-based view by passing the new url, the class-based view (imported from `.views`) modified by the `.as_view()` method and a name that identifies the view (optional) |
| **add urls from function-based views** | ![func-based view url registration](images/url-from-func.png) | Register a new url that shows a function-based view by passing the new url, the function-based view (imported from `.views`) and a name that identifies the view (optional) |

#### `app/admin.py`

| situation | what to do | description |
| --- | --- | --- |
| **models** | ![model registration](images/model-reg.png) | When you make a model that you want to be able to see and manipulate from the admin page, you need to register it with `admin.site.register(MyModel)` where `MyModel` is imported from `.models` |