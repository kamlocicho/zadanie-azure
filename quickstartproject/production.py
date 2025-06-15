import os

from .settings import *

# default local settings are overwriten here on production
# Ideally the databse connection code should be here too
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-default-key')

ALLOWED_HOSTS = [os.environ.get("WEBSITE_HOSTNAME")]
CSRF_TRUSTED_ORIGINS = [os.environ.get("WEBSITE_HOSTNAME")]
DEBUG = False

INSTALLED_APPS += ['storages']
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME=os.environ['AZURE_ACCOUNT_NAME']
AZURE_ACCOUNT_KEY=os.environ['AZURE_ACCOUNT_KEY']
AZURE_CONTAINER=os.environ['AZURE_CONTAINER']
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'