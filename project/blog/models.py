from django.db import models

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()

	def __unicode__(self):
		return self.title

class Answer(models.Model):
	question = models.ForeignKey(Question, related_name='answers')
	answer = models.TextField()
	# make votes readonly in admin and templates
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.answer[:80]
