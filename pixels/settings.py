from pathlib import Path
import os
from dotenv import load_dotenv
import  cloudinary_storage 

import dj_database_url
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nx0javx)r^1valaxr8j-f%^33dc2*hao8whc$0hq+f%$@h7%+@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', True) 
# DEBUG = True





# Additional security settings
if not DEBUG:
    # Ensure allowed hosts are set correctly
    ALLOWED_HOSTS = ['pixelvault.live','www.pixelvault.live']

    # Security middleware settings
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True 
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'

    # Configure logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': '/path/to/your/logfile.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'pix.apps.PixConfig',
    'multiupload',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pixels.urls'

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

WSGI_APPLICATION = 'pixels.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DB_URL") ),
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

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

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT  = "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = 'main_sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_SECURE = True

ADMIN_SESSION_COOKIE_NAME = 'admin_sessionid'
ADMIN_SESSION_COOKIE_PATH = '/admin'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False #was originally true

LOGIN_REDIRECT_URL = '/Dashboard'



# import socket
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# def send_data(client_socket, data):
#     try:
#         client_socket.sendall(data)
#     except socket.error as e:
#         if e.errno == 32:  # Broken pipe error
#             logging.error("Broken pipe error: %s", e)
#         else:
#             logging.error("Socket error: %s", e)

# # Example server setup
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 64216))
# server_socket.listen(1)

# while True:
#     client_socket, address = server_socket.accept()
#     logging.info("Connection from %s", address)
#     try:
#         send_data(client_socket, b"Hello, World!")
#     except Exception as e:
#         logging.error("An error occurred: %s", e)
#     finally:
#         client_socket.close()

# import socket
# import logging
# import traceback

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# def send_data(client_socket, data):
#     try:
#         client_socket.sendall(data)
#         logging.info("Data sent to client")
#     except socket.error as e:
#         if e.errno == 32:  # Broken pipe error
#             logging.error("Broken pipe error: %s", e)
#         else:
#             logging.error("Socket error: %s", e)
#     except Exception as e:
#         logging.error("Unexpected error: %s", traceback.format_exc())

# # Example server setup
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 64216))
# server_socket.listen(1)

# while True:
#     client_socket, address = server_socket.accept()
#     logging.info("Connection from %s", address)
#     try:
#         send_data(client_socket, b"Hello, World!")
#     except Exception as e:
#         logging.error("An error occurred: %s", e)
#     finally:
#         client_socket.close()
#         logging.info("Client connection closed")

CLOUDINARY_STORAGE = {
    'CLOUD_NAME' : 'dlgcq9sqc',
    'API_KEY' : '375753421484816',
    'API_SECRET' : '2QVjjFccIVr6MuFp2Fdp9ksO-qs',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'