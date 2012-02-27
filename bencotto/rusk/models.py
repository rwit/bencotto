from django.db import models
from django.contrib.auth.models import User

class rusk(models.Model):
    user = models.ForeignKey(User, unique=False, verbose_name='submitted by')
    title = models.CharField(max_length=64)
    description = models.TextField()
#@todo notice requires python imaging library
#    image = models.ImageField()
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title

class likes(models.Model):
    user = models.ForeignKey(User)
    rusk = models.ForeignKey(rusk)
    
    class Meta:
        unique_together = ('user', 'rusk')
    
class comments(models.Model):
    user = models.ForeignKey(User)
    rusk = models.ForeignKey(rusk)
    comment = models.CharField(max_length=128)
    
    def __unicode__(self):
        #c = {'rusk':self.rusk, 'user':self.user, 'comment':self.comment}
        #return str(c)
        return self.comment 
    
    class Meta:
        unique_together = ('user', 'rusk')
