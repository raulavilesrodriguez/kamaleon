# KAMALEON APP
Este back-end es realizado por industrias Cochitas Raúl Avilés S.A.

```
📦 PROYECTO 
    ┣ 📦BACK-END (Django)
    ┃    ┣ 📂kamaleon (App)
    ┃    ┃  ┣  📜models.py ()
    ┃    ┃  ┣  📜admin.py
    ┃    ┃  ┣  📜serializers.py
    ┃    ┃  ┣  📜admin.py
    ┃    ┃  ┣  📜urls.py
    ┃    ┃  ┣  📜....
    ┃    ┣ 📂project_marketing
    ┃    ┃  ┣  📜settings.py
    ┃    ┃  ┣  📜urls.py
    ┃    ┃  ┣  📜....

```
## Instrucciones de Implementación

### Paquetes Instalados
Framework:
- django: The Django framework is the backbone of the this project final.

Packages for building an API:
- django-rest-framework: To serialize data and turn our Django application into a RESTful API.

Packages for authentication:
- django-rest-auth: Endpoints needed for user authentication.
- django-allauth: Needed for user registration.
- django-cors-headers: To specify domains where requests can be made from.

Package for calculating the cumulative sum of a matrix:
- pandas: Cumulative sum of a column in Pandas can be calculated with the use of a function cumsum().

```sh
pipenv install django djangorestframework django-rest-auth django-allauth django-cors-headers pandas
```
- Create the Django project:
```sh
django-admin startproject project_marketing .
```
Note the period at the end of the command. This will create the project in the current directory instead of making a whole new one.

- Terminate the development server in terminal and run the following command to create the app:
```sh
python manage.py startapp kamaleon
```
Instalar para poder usar variables de entorno, ahí es donde guardaremos la información en relación con la conexión a la base de datos:
```sh
pipenv install django-environ
```

Install the following packages to upload to Heroku:
OJO Todos los paquetes se deben instlar en pipenv, sino no funciona en Heroku. Si aprece un error import fcntl en el log de Heroku, instalar en ubuntu (El uso del subsistema de Windows para Linux (WSL) en Windows 10) gunicorn. 
- gunicorn. La librería más importante de todas, me refiero a gunicorn. gunicorn es un servidor HTTP para Unix, sin él, será prácticamente imposible realizar el despliegue.
```sh
pipenv install gunicorn
```
- psycopg2. El gestor de base de datos PostgreSQL.
```sh
pipenv install psycopg2
```
- dj-database-url. Para realizar la conexión entre el proyecto y el gestor de base de datos usaremos la librería dj-database-url, esto principalmente, ya que Heroku nos proveerá de una base de datos que no se encuentra en el mismo servidor.
```sh
pipenv install dj-database-url
```
- python-decouple. Para que podamos iniciar el servidor haremos uso de ciertas variables de entorno.
```sh
pipenv install python-decouple
```
Instalamos WhiteNoise. Django no soporta servir archivos estáticos en producción, así que nos apoyaremos de WhiteNoise.
```sh
pipenv install whitenoise
```

Create requirements.txt file:
```sh
pip freeze > requirements.txt
```

Tip: Una forma en la cual puedes instalar todas las dependencias de un proyecto sin tener que instalar librería por librería, será ejecutando la siguiente sentencia (El archivo requirements.txt ya deberá existir).

```sh
pip install -r requirements.txt
```

### Settings - To work with Heroku
Para que funcione con Heroku:
- En el archivo settings.py
```python
import environ
import os
from decouple import config

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY', default=env('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DJANGO_DEBUG', default=env('DJANGO_DEBUG'), cast=bool)

ALLOWED_HOSTS = ['*']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    .......
]

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

# PROJECT_ROOT and STATIC_ROOT to up to HEROKU. Para que funcione el CSS
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

if config('DJANGO_PRODUCTION', default=False, cast=bool):
    from .settings_production import *
```
- En el archivo settings_production.py:
```python
import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
```
- OJO: se debe crear el archivo Procfile:
```sh
echo "web: gunicorn project_marketing.wsgi" > Procfile
```
En el archivo Procfile también colocar lo siguiente para que las migraciones sean automáticas:
```sh
release: python manage.py makemigrations 
release: python manage.py migrate
```
- Crear un archivo runtime.txt (no es tan necesario ya que Heroku actualmente implementa la última versión de python)

```sh
echo "python-3.9.2" > runtime.txt
```
- Crear el archivo .gitignore. Ahí colocar los arhivos a ignorar.

- Si aparece el error at=error code=H14 desc="No web processes running", ejecutar:
```sh
heroku ps:scale web=1
```
Este error aparece cuando no está instalado en el entorno virtual gunicorn.

### Heroku
- Instalar Heroku
```sh
brew install heroku/brew/heroku
```
- Get the Heroku Command Line Interface. Es lo mismo del comando de instalación de arriba.
```sh
curl https://cli-assets.heroku.com/install.sh | sh
```
- Create a new Git repository for this project.
```sh
git init
```
- Login to Heroku CLI.
```sh
heroku login
```
- Crear nuestra aplicación.
```sh
heroku create <nombre de tu aplicación heroku>
```
- Ligamos el repositorio a nuestra app en heroku.
```sh
heroku git:remote -a <nombre de tu aplicación heroku>
```
- Crear nuestra base de datos en Heroku. Se puede hacer también a través de la página web de Heroku.
```sh
heroku addons:create heroku-postgresql:hobby-dev
```
- Add your project’s files to Git
```sh
git add .
```
- Commit the files to Git.
```sh
git commit -am "Initialize Django project"
```
- Push the files to the Heroku repository
```sh
git push heroku master
```
- Para chequear si hay errores
```sh
heroku logs --tail
```
- Para crear el super usuario y hacer migraciones. Hacerlo en el terminal de Ubuntu
```sh
heroku run bash
```
```sh
python manage.py migrate
python manage.py createsuperuser
```

### Executing this project
Then, start the server (local)
```sh
python manage.py runserver
```
