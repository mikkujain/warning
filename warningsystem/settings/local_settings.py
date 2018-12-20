from warningsystem.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'warningsystem.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'collected-static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
