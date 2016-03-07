# healthblog
This runs Python 3 and django 1.8
To install, at the terminal
> git clone https://github.com/jrthorne/healthblog.git <YOUR DIR>
Create a virtual environment with
> python3 -m venv ~/.virtualenvs/<MYPYTHONENVNAME>
where "healthblog" is a good choice for MYPYTHONENVNAME. If you have workon setup
> workon healthblog
(healthblog) >

Now you need to add a local.py file to /project/settings to contain your google and facebook secret keys, and the site ID
if you are running this with DEBUG = False (NOTE: I may have this set to true in project/settings/__init__.py)

Even without proper values for the secrets and keys, I beleive you can run this with manage.py runserver on port 8000, but
you would have to create your own posters, and register the Poster model in admin.py

This is for registration of users. I could not use django-register, as (last time I cheked) this was not available for 
python 3.
Example local.py:
import sys
globals().update(vars(sys.modules['settings']))

# to install a local only application
#INSTALLED_APPS += ('another_app',)

SITE_ID = 1

DEBUG=True
# don't send emails from development machine
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIAL_AUTH_FACEBOOK_KEY = 'YOURS'
SOCIAL_AUTH_FACEBOOK_SECRET = 'YOURS'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "YOURS.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "YOURS"

