from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.http import Http404


# Create your models here.
class Poster(models.Model):
    # one to one with django user. You can select any user to be a player
    user = models.OneToOneField(User, related_name='poster')

    def __str__(self):
        try:
            first_name = self.user.first_name
            provider = self.user.social_auth.first().provider
        except User.DoesNotExist:
            first_name = "Does Not Exist"
            provider = "Does Not Exist"
        
        return '%d: %s: %s' % (self.id, first_name, provider)


class Question(models.Model):
    when_asked = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    original_poster = models.ForeignKey(Poster, related_name='op')

    @property
    def vote_max(self):
        maxVote = self.answers.aggregate(Max('votes'))['votes__max'] or 0
        return maxVote

    @property
    def num_ans(self):
        num_ans = self.answers.count()
        return num_ans

    # remember, don't use __unicode__ if using python 3
    def __str__(self):
        return self.title

    """ If the compare user is not the owner, raise 404 or return not
    authorised message """
    def authorized_owner_or_404(self, compare_user):
        if compare_user != self.original_poster.user:
            raise Http404
        return


class Answer(models.Model):
    when_answered = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Poster, related_name='author')
    question = models.ForeignKey(Question, related_name='answers')
    answer = models.TextField()
    # make votes readonly in admin and templates
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer[:80]

    def authorized_owner_or_404(self, compare_user):
        if compare_user != self.author:
            raise Http404
        return
