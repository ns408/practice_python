# Projects

## Project Learning Log

```shell
mkdir project_learning_log
cd project_learning_log

echo 'venv/*' > .gitignore
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

### Defining the Entry Model

Add the `class Entry` to `learning_log/models.py`

### Migrating the Entry Model

```shell
python manage.py makemigrations learning_logs
python manage.py migrate
```

### Registering Entry with the Admin Site

Modify `admin.py` and add Entries from http://127.0.0.1:8000/admin/

### Django shell

```shell
python manage.py shell

# Import Topic and Entry from learning_logs.models module
from learning_logs.models import Topic, Entry

# List me all topics
for topic in Topic.objects.all():
    print(topic.id, topic, topic.date_added)

# List me all entries
for entry in Entry.objects.all():
    print(entry.id, entry, entry.date_added)

# Lookup entries for a certain topic
Topic.objects.get(id=1).entry_set.all()
```

### Project Pizzeria

Create and Start project

```shell
mkdir project_pizzeria
cd project_pizzeria

echo 'venv/*' > .gitignore
python3 -m venv venv
source venv/bin/activate

pip install django

django-admin startproject pizzeria .
ls pizzeria

python manage.py migrate

python manage.py runserver 8010
```

Starting the app

```shell
source venv/bin/activate

python manage.py startapp pizzas
ls pizzas
```

Include app in the overall project by editing `pizzeria/settings.py`

Modify `pizzas/models.py` and define:
- a model Pizza with a field called `name`.
- a model called Topping with fields called `pizza` and `name`.

Create and apply the migration

```shell
python manage.py makemigrations pizzas
python manage.py migrate
```

Create a SuperUser

`python manage.py createsuperuser`

Registering Models with the Admin Site

Modify `learning_log/admin.py` and access http://127.0.0.1:8010/admin/

Django shell

```shell
python manage.py shell

# Import Topic and Entry from learning_logs.models module
from pizzas.models import Pizza, Topping

# List me all pizzas
for pizza in Pizza.objects.all():
    print(pizza.id, pizza)

# List me all toppings
for topping in Topping.objects.all():
    print(topping.id, topping)

# Lookup toppings for a certain pizza
Pizza.objects.get(id=1).topping_set.all()
```

### Making Pages

- define URLs
- write views
- write templates

URL maps to view. View function retrieves and processes the data needed for the page.
View function renders the page using a template which contains overall structure of the page.

#### Mapping a URL

Modify `learning_log/urls.py`
Create `learning_logs/urls.py`

#### Writing a View

Modify `learning_logs/views.py`

#### Writing a Template

```shell
mkdir -p learning_logs/templates/learning_logs
cat > learning_logs/templates/learning_logs/index.html <<EOF
<p>Learning Log</p>

<p>Track your learning.</p>
EOF
```

### Project Meal Planner

Create and Start project

```shell
mkdir project_meal_planner
cd project_meal_planner

echo 'venv/*' > .gitignore
python3 -m venv venv
source venv/bin/activate

pip install django

django-admin startproject meal_planner .
ls meal_planner

python manage.py migrate

python manage.py runserver 8020
```

**Starting the app**

```shell
source venv/bin/activate

python manage.py startapp meal_plans
ls meal_plans
```

Include app in the overall project by editing `meal_planner/settings.py`

**Mapping a URL**

Modify `meal_planner/urls.py`
Create `meal_plans/urls.py`

**Writing a View**

Modify `meal_plans/views.py`

**Writing a Template**

```shell
mkdir -p meal_plans/templates/meal_plans
cat > meal_plans/templates/meal_plans/index.html <<EOF
<p>Meal Planner</p>

<p>Plan your meals.</p>
EOF
```

### Project Pizzeria Home Page

```shell
source venv/bin/activate

python manage.py runserver 8010
```

**Mapping a URL**

Modify `pizzeria/urls.py`
Create `pizzas/urls.py`

**Writing a View**

Modify `pizzas/views.py`

**Writing a Template**

```shell
mkdir -p pizzas/templates/pizzas
cat > pizzas/templates/pizzas/index.html <<EOF
<p>Pizzeria</p>

<p>Order your pizzas.</p>
EOF
```

### Template Inheritence

```shell
touch learning_logs/templates/learning_logs/base.html
vim learning_logs/templates/learning_logs/index.html
```

### The Topics Page

Two pages:
- general topics page
- page to display entries for a single topic

####  The Topics URL Pattern

Modify `learning_logs/urls.py`

#### The Topics View

Modify `learning_logs/views.py`

#### The Topics Template

Create `learning_logs/templates/learning_logs/topics.html`
Modify `learning_logs/templates/learning_logs/base.html`
