import os
from decouple import config, Csv
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("SECRET_KEY")

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',


    # internal apps
    "journal.accounts",  # renamed at journal/accounts/apps.py
    "journal.main_core",
    "journal.entries"


]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


AUTH_USER_MODEL = "accounts.User"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static_files"
# this tells django where to find your static folders
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = config("EMAIL_BACKEND")
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# # Sites

SITE_ID = 1

# django-allauth

# ACCOUNT_ADAPTER => default
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS => default
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL => default
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL => default
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS => default
# ACCOUNT_EMAIL_CONFIRMATION_HMAC => default
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Saas Name - "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = config("ACCOUNT_DEFAULT_HTTP_PROTOCOL")
# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN => default
# ACCOUNT_EMAIL_MAX_LENGTH => default
# ACCOUNT_MAX_EMAIL_ADDRESSES => default
# ACCOUNT_FORMS => default
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT => default
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT => default
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# ACCOUNT_LOGOUT_ON_GET => default
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE => default
# ACCOUNT_LOGIN_ON_PASSWORD_RESET => default
# ACCOUNT_LOGOUT_REDIRECT_URL => default
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE => default
ACCOUNT_PRESERVE_USERNAME_CASING = False
# ACCOUNT_PREVENT_ENUMERATION => default
# ACCOUNT_RATE_LIMITS => default
ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE => default
# ACCOUNT_SIGNUP_FORM_CLASS => default
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_SIGNUP_REDIRECT_URL => default
# ACCOUNT_TEMPLATE_EXTENSION => default
# ACCOUNT_USERNAME_BLACKLIST => default
# ACCOUNT_UNIQUE_EMAIL => default
def ACCOUNT_USER_DISPLAY(user): return user.email  # noqa


# ACCOUNT_USER_MODEL_EMAIL_FIELD => default
# ACCOUNT_USER_MODEL_USERNAME_FIELD => default
# ACCOUNT_USERNAME_MIN_LENGTH => default
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USERNAME_VALIDATORS => default
# SOCIALACCOUNT_* => default

# # django-extensions

# GRAPH_MODELS = {
#     "app_labels": ["accounts", "core", "entries"],
#     "rankdir": "BT",
#     "output": "models.png",
# }
