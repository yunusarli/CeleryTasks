# DJANGO REST API WITH CELERY AND REDIS

In this project i try to use celery as worker and redis as broker to manage asyncronous tasks in django.

## Installation

First of all, redis and celery is an obligation. Celery is directly comes with requirements.txt file because it is actually a python package. But, Celery needs a broker to work with. In this project i used Redis. To start redis install directly or in docker write

```bash
docker run -p 6379:6379 redis
```
Now you are ready to go.
Install the requirements.txt

```bash
pip install -r requirements.txt
```
And as last step start Celery. Go into project level directory (manage.py should be in the same directory)

```bash
celery -A CeleryTasks worker --loglevel=INFO --concurrency 1 -P solo
```

## Usage
There is two different app and signals in this project. One of them is mail sender and the other one is file uploader.When an instance saved in the database Celery start to work on background tasks and server can accept new requests.
Go into project directory (same manage.py)
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
