"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
from django.contrib import messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p!ot_a&yi7#4)fiho8*q29^w=ot-k71=l*!g#g%rmzjn^$eulu'
# EPgkXXwi03nu4Rq4oYd14SoESEsciI9ubYEkt9ef0FUPPUkKfXbjVIKhXwDTN5OAVwxmMhvFEe3wV7f9

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True#DEBUG = config('DEBUG', default=True, cast=bool) #True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',

            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT  = BASE_DIR /'static'
STATICFILES_DIRS = [
    'myproject/static',

]


# media fieldsets
MEDIA_URL = '/media/'
MEDIA_ROOT  = BASE_DIR /'media'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


# SMTP configuration
EMAIL_HOST =  'smtp' #config('EMAIL_HOST')
EMAIL_PORT =  587 #config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = 'signin1022@gmail.com' #config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = 'Mypassword@1998' #config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True #config('EMAIL_USE_TLS', cast=bool)
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
