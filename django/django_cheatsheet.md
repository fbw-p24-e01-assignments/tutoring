## Django Cheatsheet

#### When and where to use the Django files

##### `settings.py`

| situation | what to do | description |
| --- | --- | --- |
| **apps** | ![app registration](images/apps.png) | After creating an app with `django-admin startapp`, you need to register it as in the `INSTALLED_APP` list |
| **databases** | ![database registration](images/db.png) | To connect to a database, you have to register its engine (`postgres_psycopg2`), name (`my_db`), user to be accessed as, password of the user, host (`'127.0.0.1'` for localhost) and port (optional, `'5432'` for postgres) |
| **static files** | ![static file dir registration](images/static.png) | If your static folder is outside of your app, you need to register the folder by adding the variable `STATICFILES_DIRS`, which is going to be a list containing a string path to the folder |
| **templates** | ![templates registration](images/templates.png) | If you want to use templates, you have to register them in the `'DIRS'` key of the `TEMPLATES` variable as a path to the folder |