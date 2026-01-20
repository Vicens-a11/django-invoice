from pathlib import Path

# ------------------------------------------
# BASE_DIR
# ------------------------------------------
# Chemin absolu vers la racine du projet (dossier contenant manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------
# Secret & Debug
# ------------------------------------------
SECRET_KEY = 'django-insecure-m9)j@b@6ykq1w_*nf#d_duimee1#4=)b_nx%-rvma$l!#%z=#a'
DEBUG = True
ALLOWED_HOSTS = []

# ------------------------------------------
# Applications installées
# ------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'fact_app',  # ton application principale
]

# ------------------------------------------
# Middleware
# ------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------
# URLs et WSGI
# ------------------------------------------
ROOT_URLCONF = 'django_invoice.urls'
WSGI_APPLICATION = 'django_invoice.wsgi.application'

# ------------------------------------------
# Templates
# ------------------------------------------
TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # templates globaux
        'APP_DIRS': True,          # templates dans les apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ------------------------------------------
# Base de données (SQLite)
# ------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------------------
# Password validation
# ------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------
# Internationalization
# ------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------
# Fichiers statiques (CSS, JS, images)
# ------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'  # pour collectstatic en production

# ------------------------------------------
# Fichiers Media (uploads utilisateurs)
# ------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------------------------
# DEBUG: servir les fichiers MEDIA en développement
# ------------------------------------------
# A mettre dans urls.py du projet
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
