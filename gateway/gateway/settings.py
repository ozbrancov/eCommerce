"""
Django settings for gateway project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-qm_^6pyz_lnyh7+@c#axps6zjs=g@(l&s_0v74(((=o_cer*%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hangout',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gateway.urls'

WSGI_APPLICATION = 'gateway.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hangout',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'oliver',
        'PASSWORD': 'vision',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates"),
    )

#MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static", "media")
#MEDIA_URL = "/media/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static", "static_only")
STATIC_URL = '/static/'

STATIC_FILES_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "static"),
    )



