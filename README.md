# Mountains Backend Project
This is a [Django REST framework](http://www.django-rest-framework.org/) project for storing and retrieving mountain peaks.

## Installation (Docker)
After you cloned the repository, you want to :
1. Step 1 : execute the command below to build the images
```
sudo docker-compose build
```

Ths dockerfile use image **python:3.8-slim** then install the necessary dependencies for PostgreSQL to work properly with Django.

After that, it install all the required dependencies in fil requirements.txt

2. Step 2 : Generate a database for our API model (migrations)

```
sudo docker-compose run django_mountains sh -c "python manage.py makemigrations"
```
```
sudo docker-compose run django_mountains sh -c "python manage.py migrate"
```

3. Step 3: once the postgreSQL database is created and tables are generated, all you need to do is run your Django container

```
sudo docker-compose up
```
## Endpoints

We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)

`GET http://0.0.0.0:8000/mountains/`

`POST http://0.0.0.0:8000/mountains/` 

this is a body example to add a new mountain peak:
```
{
    "name": "Mount Everest",
    "altitude":8849,
    "lat": 27.986065,
    "long": 86.922623
}
```

`DELETE http://0.0.0.0:8000/mountains/<mountain_id>/` 
## Local running requirements
For local testing, you have to some packages (Python 3.8 / Django 3.1 /Django REST Framework
) 

And make sure to use a local database (change your settings.py).

First, create a virtual environment 
```
python -m venv env
```

Second, install all the required dependencies by running

```
pip install -r requirements.txt
```

Last but not least start up Django's development server.
```
python manage.py runserver
```
