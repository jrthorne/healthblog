from django.contrib import auth
from social.apps.django_app.default.models import UserSocialAuth
from social.exceptions import AuthAlreadyAssociated
from django.contrib.auth.models import User
from apps.blog.models import Poster


def create_poster(backend, details, response, user=None, *args, **kwargs):
    """
    Any social auth cretaed user should be a poster
    """
    if user and user.pk:
        try:
            old_poster = user.poster
        except Poster.DoesNotExist:
            # User exists, poster does not. Create poster
            new_poster = Poster(user=user)
            new_poster.save()
        
        return {
            'user': user,
            'is_new': False,
        }
    else:
        
        return {
            'user': user,
            'is_new': False,
        }