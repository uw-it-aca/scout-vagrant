# Local settings for server_proj project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
JSON_PRETTY_PRINT = False

OAUTH_AUTHORIZE_VIEW = 'spotseeker_server.views.oauth.authorize'
OAUTH_CALLBACK_VIEW = 'spotseeker_server.views.oauth.callback'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

LABSTATS_URL = ""

# Values can be one of 'all_ok' or 'oauth'. If using 'oauth', client applications will need an oauth key/secret pair.
SPOTSEEKER_AUTH_MODULE = 'spotseeker_server.auth.all_ok'
#SPOTSEEKER_AUTH_MODULE = 'spotseeker_server.auth.oauth'
SPOTSEEKER_AUTH_ADMINS = (
    "labstats_daemon",
    "scout_manager",
)

# Custom validation can be added by adding SpotForm and ExtendedInfoForm to org_forms and setting them here.
SPOTSEEKER_SPOT_FORM = 'spotseeker_server.org_forms.uw_spot.UWSpotForm'
SPOTSEEKER_SPOTEXTENDEDINFO_FORM = 'spotseeker_server.org_forms.uw_spot.UWSpotExtendedInfoForm'
SPOTSEEKER_SEARCH_FILTERS = ['spotseeker_server.org_filters.uw_search.Filter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'server.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will not format dates, numbers and
# calendars accoring to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://localhost:8000/media/'

# Absolute path to the directory static files should be collected tp.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations for static files
STATICFILES_DIRS = (
    # Put strings here
    # Always use forward slashes, even on Windows
    # Don't forget to use absolute
)

# List of finder classes that know how to find static files in
#various locations.
STATICFILES_FINDER = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ server_key }}'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

ROOT_URLCONF = 'serverproject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'serverproject.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "home/html/django_templates"
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'sposeeker_server'
    }
}

CACHE_MIDDLEWARE_SECONDS = 60 * 60 # Cache what we can for an hour

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'spotseeker_server',
    'oauth_provider',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/home/ubuntu/spacescout_server.log',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Preferred web app hostname
SS_APP_SERVER = 'spotseeker-test.uw.edu'

# Path used by web app to display a space
SS_APP_SPACE_PATH = "/space/{% raw %}{{ spot_id }}{% endraw %}/{% raw %}{{ spot_name }}{% endraw %}"
