URL parser
This program collects url's from a given initial web link (URL)

* Python 3.8
* Django 3.1.2
* PostgreSQL 10

To run this project locally:

Para rodar o projeto localmente:

* git clone https://github.com/MarqQ/url_parser.git
* start a virtual env with Python 3.
* activate virtualenv.
* install requirements.
* run migrate/migrations.

LINUX
```
git clone
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

WINDOWS
```
git clone
python3 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

This program collects related URL's from a given initial web link (URL).
- The main URL given will be stored in a relational DB
- The URL collected from main URL will be stored in a CSV file with a unique 32-char filename
- The 32-char csv filename will be stored in DB related to the main URL as reference
- The csv file will be stored in a specific folder
- All main URL's and related URL's appears in the html page that user give an URL


