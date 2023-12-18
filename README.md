# Litrevu

This project consists of creating a website for the company LITReview. The purpose of the web application is to allow users to request and post reviews of books or articles.


## Creating Virtual environment, downloading and running the program:

```bash
git clone https://github.com/lethyxnekuia/litrevu.git
cd litrevu
poetry install
poetry shell
cd litrevu
python manage.py migrate
python manage.py runserver
```

* server : http:/127.0.0.1:8000/

## Admin:

* link : http:/127.0.0.1:8000/admin

* create a user : 
```bash
python manage.py createsuperuser
```

## Technology:

- **Framework :** Django
- **Base de données :** SQLite 
- **Langage :** Python 
- **Front-end :** HTML, CSS, JavaScript


## Flake8:

```bash
flake8 litrevu
```
