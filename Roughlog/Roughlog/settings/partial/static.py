import os

from .application import PROJECT_ROOT_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'Roughlog', 'static'),
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')

# PIPELINE

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'application': {
            'source_filenames': (
              'css/roughlog/*.css',
            ),
            'output_filename': 'css/roughlog.css',
        },
        'vendor': {
            'source_filenames': (
              'css/vendor/*.css',
            ),
            'output_filename': 'css/vendor.css',
        },
    },
    'JAVASCRIPT': {
        'application': {
            'source_filenames': (
              'js/roughlog/*.js',
            ),
            'output_filename': 'js/roughlog.js',
        },
        'vendor': {
            'source_filenames': (
              'js/vendor/*.js',
            ),
            'output_filename': 'js/vendor.js',
        },
    },
}
