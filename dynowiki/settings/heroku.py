"""
Production Settings for Heroku
"""

import environ
from dynowiki.settings.local import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# # reading .env file
# environ.Env.read_env()

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}

# S3 EXAMPLE
# This config is for S3 storage - only enable for media, and only use if you've
# set up an account with Amazon or have added the Bucketeer addon.
# Example taken from https://stackoverflow.com/questions/19915116/setting-django-to-serve-media-files-from-amazon-s3
# with credit for being a very concise S3 tutorial
INSTALLED_APPS += ('storages',)

AWS_STORAGE_BUCKET_NAME = env('BUCKETEER_BUCKET_NAME')
# Bucketeer requires media files to be in public to be generally accessible
S3_URL = f"http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/public/"
MEDIA_URL = f"{S3_URL}{MEDIA_ROOT}/"
DEFAULT_FILE_STORAGE = 'dynowiki.s3utils.MediaRootS3BotoStorage'
wiki.conf.settings.STORAGE_BACKEND='dynowiki.s3utils.MediaRootS3BotoStorage'
wiki.plugins.images.settings.IMAGE_PATH = f"{MEDIA_URL}/wiki/images"
AWS_ACCESS_KEY_ID = env('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('BUCKETEER_AWS_SECRET_ACCESS_KEY')