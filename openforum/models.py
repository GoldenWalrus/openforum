from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # class methods
    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    # class methods
    def __unicode__(self):
        return self.name

class Question(models.Model):
    questiontext = models.CharField(max_length=200)
    # questionnumber = models.IntegerField(default=0)
    date = models.DateTimeField('date published')
    sticky = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    board = models.ForeignKey(Board)
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
