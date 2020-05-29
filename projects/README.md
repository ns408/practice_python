# Projects

## Project Learning Log

```shell
mkdir project_learning_log
cd project_learning_log

python3 -m venv venv
source venv/bin/activate

pip install django
```

### Create and Start project

```shell
django-admin startproject learning_log .
ls learning_log

# Create/Migrate the database
python manage.py migrate

# runserver
python manage.py runserver 8000
```

### Starting an app

```shell
source venv/bin/activate

# start the app
# instruct Django to create the infrastructure to build an app
python manage.py startapp learning_logs
ls learning_logs
```

### Activate Models

Include our app in the overall project by editing `learning_log/settings.py`

#### Modify the database so it can store information related to the model Topic.

Create the migration

`python manage.py makemigrations learning_logs`

Apply the migration

`python manage.py migrate`

### Django Admin Site

Work with models through admin site.

#### Setting up a SuperUser

`python manage.py createsuperuser`

### Registering a Model with the Admin Site

Modify `learning_log/admin.py` and access http://127.0.0.1:8000/admin/

