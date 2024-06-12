"""
Django settings for winenot_backend project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta, datetime
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=y5@_ddwbn74c4sh#7nccp5z0unn+1zjkmsx3(1y=&hq2@&0r)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', 'api.winenot.com', 'wine-not.netlify.app']

#Url for the frontend
WEBSITE_URL = 'http://localhost:5173'



# Application definition

AUTH_USER_MODEL = 'account.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=270),
    'ROTATE_REFRESH_TOKENS': False,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://wine-not.netlify.app",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    "http://wine-not.netlify.app",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:10000",
    "http://localhost:5173",
    ]

#HEY DEVS: Comment out the django.contrib.saticfiles line to run the app locally.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'collexn',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'winenot_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI_APPLICATION = 'winenot_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
#For running fully in production:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        **dj_database_url.config(
            default='postgres://django_app_db_p0lm_user:mFUdWdpT4kXyMh833Qi8hhtVm0lrJTQl@dpg-cpkaglq0si5c73cngoog-a/django_app_db_p0lm',
            conn_max_age=600
        )
    }
}

#For running locally but using the production database:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         **dj_database_url.config(
#             default='postgres://django_app_db_p0lm_user:mFUdWdpT4kXyMh833Qi8hhtVm0lrJTQl@dpg-cpkaglq0si5c73cngoog-a.oregon-postgres.render.com/django_app_db_p0lm',
#             conn_max_age=600
#         )
#     }
# }

# For running locally:  (Make sure to create a database called 'winenot' and have it running)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'winenot'
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# HEY RENDER USERS: Uncomment the following SECTION to enable HTTPS on your Render deployment.  To run it locally comment it out.
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/

# # This setting informs Django of the URI path from which your static files will be served to users
# # Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
# STATIC_URL = 'wine-not.netlify.app/static/'

# # This production code might break development mode, so we check whether we're in DEBUG mode
# if not DEBUG:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#     # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
#     # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
#     # and renames the files with unique names for each version to support long-term caching

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
