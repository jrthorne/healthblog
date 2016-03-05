from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    original_poster = models.ForeignKey(User, related_name='op')

    @property
    def answer_max_votes(self):
        maxVote = self.answers.aggregate(Max('votes'))['votes__max']
        return maxVote
    
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    author = models.ForeignKey(User, related_name='author')
    question = models.ForeignKey(Question, related_name='answers')
    answer = models.TextField()
    # make votes readonly in admin and templates
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.answer[:80]
