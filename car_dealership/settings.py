import os

ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .settings_prod import *
else:
    from .settings_dev import *
    
        