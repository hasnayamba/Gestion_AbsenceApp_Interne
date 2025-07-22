import os
from pathlib import Path
from urllib.parse import urlparse

# --- Chemins de base ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Clé secrète Django ---
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("La variable d'environnement SECRET_KEY n'est pas définie.")

# --- Mode DEBUG ---
DEBUG = True  # ⚠️ Passe à False en production et utilise ALLOWED_HOSTS

ALLOWED_HOSTS = ["gestionabsences.azurewebsites.net", "127.0.0.1", "localhost"]

# --- Applications Django ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'absences',  # Ton app principale
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_absencesApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestion_absencesApp.wsgi.application'

# --- Base de données depuis AZURE_POSTGRESQL_CONNECTIONSTRING ---
import os
from urllib.parse import urlparse, parse_qs

def parse_database_url(url):
    if not url:
        raise RuntimeError("❌ La variable AZURE_DATABASE_URL est vide ou non définie.")

    result = urlparse(url)

    if result.scheme != "postgres":
        raise RuntimeError("❌ Seul le schéma 'postgres' est supporté dans AZURE_DATABASE_URL.")

    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': result.path.lstrip("/"),
        'USER': result.username,
        'PASSWORD': result.password,
        'HOST': result.hostname,
        'PORT': result.port or 5432,
        'OPTIONS': {
            'sslmode': parse_qs(result.query).get('sslmode', ['require'])[0]
        }
    }

# 🔧 Configuration de la base
DATABASES = {
    'default': parse_database_url(os.environ.get("AZURE_DATABASE_URL"))
}



# --- Sécurité mot de passe ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internationalisation ---
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --- Fichiers statiques ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- Authentification / Redirection ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard_collaborateur'
LOGOUT_REDIRECT_URL = 'login'

# --- Clé par défaut pour les modèles ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

