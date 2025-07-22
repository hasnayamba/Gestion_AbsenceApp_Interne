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
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        env='AZURE_DATABASE_URL',
        conn_max_age=600,
        ssl_require=True
    )
}

if not DATABASES['default']:
    print("🔍 Contenu AZURE_DATABASE_URL :", os.environ.get("AZURE_DATABASE_URL"))
    raise RuntimeError("❌ La base de données n'est pas configurée correctement. Vérifie AZURE_DATABASE_URL.")



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

