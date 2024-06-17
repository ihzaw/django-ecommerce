release: python manage.py makemigrations && python manage.py migrate && python manage.py seed
web: gunicorn ecommerce_project.wsgi --log-file -