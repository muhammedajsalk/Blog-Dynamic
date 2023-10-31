web: gunicorn blog.wsgi --log-file -
worker: celery -A blog worker --loglevel=info