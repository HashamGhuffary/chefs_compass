release: python manage.py migrate && python manage.py collectstatic --no-input
web: gunicorn chefs_compass.wsgi