import os

SECRET_KEY = os.environ.get("SECRET_KEY")


bearer_token = os.environ.get("BEARER_TOKEN")

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
    }
}
