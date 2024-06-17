release: python manage.py makemigrations --noinput && python manage.py migrate --noinput && python manage.py seed --noinput
web: gunicorn ecommerce_project.wsgi --log-file -
