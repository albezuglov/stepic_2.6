from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    added_at = models.DateField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=1)
    #author = models.ForeignKey(User)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question', args=[str(self.id)])


class Answer(models.Model):
    text = models.TextField(blank=True)
    added_at = models.DateField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    def __str__(self):
        return self.text

