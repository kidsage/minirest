from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
# DEBUG = env('DEBUG')
DEBUG = False

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = env('SECRET_KEY')
def read_secret(name):
    with open('/run/secrets/' + name, 'r') as f:
        file = f.read()
        file = file.strip()
    
    return file

SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# Connect to postgresql 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'minirest',
        'USER': 'ian',
        'PASSWORD': read_secret('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': '5432',
    }
}