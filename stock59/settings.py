"""
Django settings for stock59 project.

Generated by 'django-admin startproject' using Django 3.0.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r&p3a0yq5dt(7g+55j30u3)2g56&2!a!d8*dphv%-ka9if%pna'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stock.apps.StockConfig',
    'pages.apps.PagesConfig',
    'django_dia',
   
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

ROOT_URLCONF = 'stock59.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'stock59.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'


STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'stock59/static'),

]







# Jazzmin settings

JAZZMIN_SETTINGS = {
# title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "GESTIONSTOCK Admin",
 # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
 "site_header": "INVENTORY",
 # Welcome text on the login screen
    "welcome_sign": "Welcome to GESTIONSTOCK",
 # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "GESTIONSTOCK",
# Copyright on the footer
    "copyright": "© OUISSAM",
 "topmenu_links": [

    # Url that gets reversed (Permissions can be added)
    {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

    # external url that opens in a new window (Permissions can be added)
    {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

    # model admin to link to (Permissions checked against model)
    {"model": "auth.User"},

    # model admin to link to (Permissions checked against model)
    {"model": "auth.Group"},

    # model admin to link to (Permissions checked against model)
    {"model": "auth.Permission"},

    # model admin to link to (Permissions checked against model)
    {"model": "auth.PermissionGroup"},


    ],


}



JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
    "navbar": "navbar-inverse",
    

    

}

JAZZMIN_SETTINGS["show_ui_builder"] = False 

