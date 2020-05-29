# Projects

## Learning Log

```shell
mkdir project_learning_log
cd project_learning_log

python3 -m venv venv
source venv/bin/activate

pip install django

django-admin startproject learning_log .
ls learning_log

# Migrate (modify) the database
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

Include our app in the overall project.

`learning_log/settings.py`