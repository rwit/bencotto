from django.db import models

#@todo Should be part of auth package, right?
#class users
#class groups

class rusk(models.Model):
    description = models.TextField()
#@todo notice requires python imaging library
#    image = models.ImageField()
#@todo likes should not be here because a user should be able to unlike
#    likes = models.IntegerField()
    views = models.IntegerField()
    date_added = models.DateTimeField()
    
#    def __unicode__(self):
#        .self

class rusk_comments(models.Model):
    rusk = models.ForeignKey('rusk')
    comment = models.CharField(max_length=128)
