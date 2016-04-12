import os

from .application import BASE_DIR, PROJECT_ROOT_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Roughlog', 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')
