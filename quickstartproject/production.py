import os

from .settings import *

# Configure the domain name using the environment variable
# that Azure automatically creates for us.

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = []
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = False
DEBUG = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-default-key')

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello_azure',
    'api',
    'authentication_system'
]

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ['AZURE_POSTGRESQL_NAME'],
        'HOST': os.environ['AZURE_POSTGRESQL_HOST'],
        'USER': os.environ['AZURE_POSTGRESQL_USER'],
        'PASSWORD': os.environ['AZURE_POSTGRESQL_PASSWORD'],
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}


INSTALLED_APPS += ['storages']
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME="projektjkko"
AZURE_ACCOUNT_KEY="r+3X6Opymv4qSQRXlvaoyUNWAtzbROarjOfT6yNPdSsHG/arjUmpyLOcp02YE+Si7Hx2W8hiq0oU+AStoW6vsw=="
AZURE_CONTAINER="files"
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'