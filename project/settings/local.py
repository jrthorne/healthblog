import sys
globals().update(vars(sys.modules['settings']))

# to install a local only application
#INSTALLED_APPS += ('another_app',)

SITE_ID = 1

DEBUG=True
# don't send emails from development machine
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIAL_AUTH_FACEBOOK_KEY = '1400687656913472'
SOCIAL_AUTH_FACEBOOK_SECRET = 'e2896314c57357a4e44bbdb4fa24111d'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "485028019108-12fo3i9oidr7uucjga0916i2agv8fokc.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "adOmaEjlGQ7sM3s_e9CxuRy1"

# twitter
SOCIAL_AUTH_TWITTER_KEY =  "jfQxHs26dviEU6yu6FYj35XFh"
SOCIAL_AUTH_TWITTER_SECRET = "4TwUGyleULzGPv6QPgsZL24o7HeWm4nRGCgdHv5qYAst2paKs6"
