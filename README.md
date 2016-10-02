Simple Blog
=============
Create a web page with a form that allows a question to be created -- title and description are the only fields needed. 

Once a question has been posted, it should gets its own page, where people can post answers. People can vote answers up & down. Questions should be ordered by these ratings. 

You may use any python web framework & javascript library of your choice. Make sure the code you write doesn't just do what is needed immediately, but is code you'd be happy to maintain over time. 

If any special instructions are needed to run the application, please include them in a README file. 

Bonus: 

* Allow people to edit questions once they've been posted.

# SOLUTION:
This runs Python 3 and django 1.9
To install, at the terminal
> git clone https://github.com/jrthorne/healthblog.git <YOUR DIR>
Create a virtual environment with
> python3 -m venv ~/.virtualenvs/<MYPYTHONENVNAME>
where "healthblog" is a good choice for MYPYTHONENVNAME. If you have workon setup
> workon healthblog
(healthblog) >

My solution uses authentication and registration through Facebook or Google, and for this to work, you need secret/key pairs from a google/facebook developer account. These should be put in local.py, as they are not to be made publically available. To get the secret and key, check out my blog at
http://djangowebsites.com.au/blog/facebook-django-integration/

So you need to add a local.py file to /project/settings to contain your google and facebook secret keys, and the site ID
if you are running this with DEBUG = False (NOTE: I may have this set to true in project/settings/__init__.py)

Without proper values for the secrets and keys, you can't login/regiser when you run this 
with manage.py runserver on port 8000, but the admin interface still works.

This is for registration of users. I could not use django-register, as (last time I cheked) this was not available for 
python 3.

# TESTS:
"./manage.py test blog" from healthblog root.

# DEVELOPMENT SETTINGS LOCAL.PY:
>import sys
>globals().update(vars(sys.modules['settings']))
>
># to install a local only application
>#INSTALLED_APPS += ('another_app',)
>
>SITE_ID = 1
>
>DEBUG=True
># Direct emails to console on development machine
>EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
>
>SOCIAL_AUTH_FACEBOOK_KEY = 'YOURS'
>SOCIAL_AUTH_FACEBOOK_SECRET = 'YOURS'
>
>SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
>SOCIAL_AUTH_FACEBOOK_SCOPE = [
>    'email',
>]
>
>EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
>
># google
>SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "YOURS.apps.googleusercontent.com"
>SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "YOURS"

