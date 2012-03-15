import os.path
import logging
from django.db import models
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

def createRuskImagePath(rusk, filename):
    """Generate the upload path dynamically; including the user id in the path"""
    return os.path.join('rusks', str(rusk.user.id), os.path.basename(filename))
    
class rusk(models.Model):
    user = models.ForeignKey(User, unique=False, verbose_name='submitted by')
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to=createRuskImagePath) #'uploadedImages')
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    #@todo overload save_model in admin.py ?
#    def save(self, *args, **kwargs):
#        super(rusk, self).save(*args, **kwargs)
#        
#    def delete(self, *args, **kwargs):
#        #todo delete the image files
#        super(rusk, self).save(*args, **kwargs)
        
class likes(models.Model):
    user = models.ForeignKey(User)
    rusk = models.ForeignKey(rusk)
    
    class Meta:
        unique_together = ('user', 'rusk')
        
    def __unicode__(self):
        return u'%s %s' % (self.user, self.rusk.title)
    
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
