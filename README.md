## Environment variables
DB_DEV_NAME
DB_DEV_USER
DB_DEV_PASSWORD
DB_DEV_HOST
DB_DEV_PORT

## Virtual environment
source venv/bin/activate

## Celery
### Worker
celery -A twitter worker -l INFO

### Beat
celery -A twitter beat -l INFO

## Django server
python manage.py  runserver 0.0.0.0:8000