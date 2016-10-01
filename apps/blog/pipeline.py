from django.contrib import auth
from social.apps.django_app.default.models import UserSocialAuth
from social.exceptions import AuthAlreadyAssociated
from django.contrib.auth.models import User
from blog.models import Poster

# Any social auth cretaed user should be a poster
def create_poster(backend, details, response, user=None, *args, **kwargs):
    if user and user.pk:
        try:
            oldPoster = user.poster
        except Poster.DoesNotExist:
            # User exists, poster does not. Create poster
            newPoster = Poster(user=user)
            newPoster.save()
        # end try
        
        return {
            'user': user,
            'is_new': False,
        }
    else:
        
        return {
            'user': user,
            'is_new': False,
        }
    # endif
# end create_poster