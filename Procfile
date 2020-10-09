release: python manage.py migrate
web: gunicorn thesis_project.wsgi --port=$PORT settings.wsgi:application