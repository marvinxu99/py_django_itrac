"""
Django settings for main_project project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config, Csv
# import django_heroku


AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."
SECRET_KEY = config('SECRET_KEY', default='12345')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG=True
DOMAIN = config('DOMAIN', default='DEV')

ALLOWED_HOSTS = ['192.168.0.14', '127.0.0.1', 'localhost']
#ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    'accounts.apps.AccountsConfig',
    'core.apps.CoreConfig',
    'itrac.apps.iTracConfig',

    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main_project.wsgi.application'

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('MY_GMAIL')
EMAIL_HOST_PASSWORD = config('MY_GMAIL_PASSWORD')
EMAIL_USE_SSL = True
EMAIL_PORT = 465

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# mysql wheels: https://www.lfd.uci.edu/~gohlke/pythonlibs/
# postgreSQL: https://docs.djangoproject.com/en/3.0/ref/databases/

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'winn_mysql_1',
    #    'USER': 'winter',
    #    'PASSWORD': 'winter',
    #    'HOST': 'localhost',
    #    'PORT': '',
    #     # 'OPTIONS': {
    #     #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     #     }
    #}

    #'default': {
    #   'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'winn_itrac_1',
    #    'USER': 'winter',
    #    'PASSWORD': 'winter',
    #    'HOST': 'localhost',
    #    'PORT': '5432',
    #}
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# addin the following will cause HEROU rejected to deploy????
# but works locally???heroku
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'uploaded_files_temp')
GENERATED_BARCODE__DIR = os.path.join(BASE_DIR, 'generated_codes')

STRIPE_PUBLISHABLE_KEY = 'pk_test_LBnp367Zb5XklDLhtXFg1cgr00SIM9ArGv'
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')

# Oxford Dictionaries API
OXFORD_APP_ID = config('OXFORD_APP_ID', default='')
OXFORD_APP_KEY = config('OXFORD_APP_KEY', default='')


# Configure Django App for Heroku. 
# django_heroku.settings(locals())
