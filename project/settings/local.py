import sys
globals().update(vars(sys.modules['settings']))

# to install a local only application
#INSTALLED_APPS += ('another_app',)

DEBUG=True

SITE_ID = 2
SOCIAL_AUTH_FACEBOOK_KEY = '310084849166814'
SOCIAL_AUTH_FACEBOOK_SECRET = '0ffd7b26bdf151ec04342ababc3691ee'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]


# google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "485028019108-l56dgq6pjr719oeudm6tfeccrm9e8irj.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "1B5_Yr0ZjkC_-GKc_fNuID7P"

# twitter
SOCIAL_AUTH_TWITTER_KEY =  "nb6JOZlY08hmUY4HHXtBJYhnE"
SOCIAL_AUTH_TWITTER_SECRET = "svIlsJoyQHdSd4YEklXmi04eMUqVYgWJnhycTW1eeUzXD3xPEY"
