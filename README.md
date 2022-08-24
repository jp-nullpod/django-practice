# Steps to install

- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser  
- python manage.py runserver