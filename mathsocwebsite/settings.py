"""
Django settings for mathsocwebsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    with open(os.path.join('keys_and_pws', 'secret_key')) as f:
        SECRET_KEY = f.read()
except Exception as e:
    print "No secret_key file found, using default"
    SECRET_KEY = '08ot*-$rea13!r$u@bxrs-z&(e(&!qn-p5!nu44ib@t&2!%dz@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'elections',
    'external_api',
    'frontend',
    'services',
    'tangent'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cas.middleware.CASMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
)

ROOT_URLCONF = 'mathsocwebsite.urls'

WSGI_APPLICATION = 'mathsocwebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
try:
    with open(os.path.join(BASE_DIR, 'keys_and_pws', 'database_pw')) as f:
        DATABASE_PW = f.read()
except Exception as e:
    print "No database_pw file found, will fail"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mathsoc',
        'USER': 'mathsoc',
        'PASSWORD': DATABASE_PW,
        'HOST': 'localhost',
        'PORT': ''
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CAS_SERVER_URL = "https://cas.uwaterloo.ca/cas/"
CAS_LOGOUT_COMPLETELY = True
CAS_PROVIDE_URL_TO_LOGOUT = True

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = '/var/www/mathsocwebsite/static' ## Used for collectstatic deployments with apache
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Template files
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = {
    TEMPLATE_PATH
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mathsocbookings'
try:
    with open(os.path.join(BASE_DIR, "keys_and_pws", "mathsocbookings-gmail-pw")) as f:
        EMAIL_HOST_PASSWORD = f.read()
except: 
    print "Missing password for bookings email, won't be able to send emails to people after approving or rejecting a booking"
EMAIL_PORT = 587