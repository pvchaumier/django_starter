"""Development settings (not suited for production).

# Database

## Commands

Change names between the brackets to use the commands.
RQ: these commands have only been tested for PostgreSQL databases.

- CLI way to create a user and the db, to type as a psql superuser
psql> CREATE USER <username> WITH CREATEDB LOGIN PASSWORD <password>;
psql> CREATE DATABASE <db_name>;
psql> GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <username>;

/!\ DANGEROUS /!\
- To reinitialize the database from scratch type the following commands
psql> DROP SCHEMA public CASCADE;
psql> CREATE SCHEMA public;
psql> GRANT USAGE ON SCHEMA public TO public;
psql> GRANT USAGE ON SCHEMA public TO public;
psql> GRANT CREATE ON SCHEMA public TO public;
"""

import os

from .base import *

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Hack to make debug toolbar work with django 1.10
# see https://github.com/jazzband/django-debug-toolbar/issues/853
MIDDLEWARE_CLASSES = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
del MIDDLEWARE

# setup of the django debug toolbar
# see https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#getting-the-code
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1', '::1']
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
