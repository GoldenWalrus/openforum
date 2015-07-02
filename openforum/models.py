from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # class methods
    def __unicode__(self):
        return self.name

class Question(models.Model):
    questiontext = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    # class methods
    def __unicode__(self):
        return self.questiontext

class Response(models.Model):
    question = models.ForeignKey(Question)
    responsetext = models.CharField(max_length=400)
    date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    # class methods
    def __unicode__(self):
        return self.responsetext
