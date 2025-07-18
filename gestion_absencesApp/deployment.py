import os
from .settings import BASE_DIR
from urllib.parse import urlparse

# Récupération de la SECRET_KEY (attention au nom de la variable)
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise RuntimeError("La variable d'environnement SECRET_KEY n'est pas définie.")

# Hôte autorisé pour Azure (ou localhost par défaut)
WEBSITE_HOSTNAME = os.environ.get('WEBSITE_HOSTNAME', 'localhost')
ALLOWED_HOSTS = [WEBSITE_HOSTNAME]

# Protection CSRF
CSRF_TRUSTED_ORIGINS = [f"https://{WEBSITE_HOSTNAME}"]

DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # UNE SEULE FOIS ici !
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']

url = urlparse(connection_string)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': url.path[1:],  # retire le slash initial
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}

print("HOST utilisé pour PostgreSQL:", url.hostname)
