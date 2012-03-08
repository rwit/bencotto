from os import makedirs
import os.path
import logging
import StringIO
from PIL import Image
from django.conf import settings
#from bencotto.rusk.models import rusk

logger = logging.getLogger(__name__)

def image_processing(ruskUserId, uploadedFile):
    """
    @todo: create thumbnail
    @todo: handle file already exists
    """
    targetPath = os.path.join(settings.MEDIA_ROOT, 'rusks', str(ruskUserId), uploadedFile.name)
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    logger.debug('image_processing: {} => {}'.format(uploadedFile, targetPath))

    #May be an in-memory file or file on disk
    data = StringIO.StringIO(uploadedFile.read())
    
    #Move the original
    image = Image.open(StringIO.StringIO(data));
    #image = Image.open('/home/pbor/bencotto/bencotto/rusk/tests/data/test_image.gif');
    #Image.open(StringIO("/home/blaine/Pictures/Me/neck-beard.jpg").read()) 
    image.save(targetPath)
    
    return targetPath
#    
#>>> image = Image.open(StringIO.StringIO(data)); image.save("/home/ptarjan/www/tmp/metaward/original.png")
#
#
#file = urllib.urlopen('http://freegee.sourceforge.net/FG_EN/src/teasers_en/t_gee-power_en.gif')
#im = cStringIO.StringIO(file.read()) # constructs a StringIO holding the image
#img = Image.open(im)
#
## now use PIL
#print img.format, img.size, img.mode
#img.save('my_copy.gif')
#
## delete img if you need to save space and work on large images
#del img    
#
#    return targetPath

#
# av = self.cleaned_data['avatar']
#            resized = make_avatar(av,65)   # My custom function than returns image
#            return  InMemoryUploadedFile(resized, av.field_name, av.name, av.content_type, resized.len, av.charset)
#        
#ou can read django code for InMemoryUploadedFile "documentation". And in your resize/crop function you should use StringIO not file to save result
#        
#        
#out = im.resize((128, 128))
#
#import StringIO
#from PIL import Image
#
#im = Image.open(StringIO.StringIO(buffer))
#
#
#im.thumbnail(size, Image.ANTIALIAS)
#    im.save(file + ".thumbnail", "JPEG")
#    
#>>> data = utils.fetch("http://wavestock.com/images/beta-icon.gif")
#>>> image = Image.open(StringIO.StringIO(data)); image.save("/home/ptarjan/www/tmp/metaward/original.png")
#>>>
#>>> image = Image.open(StringIO.StringIO(data)); image.resize((36,36), Image.ANTIALIAS).save("/home/ptarjan/www/tmp/metaward/antialias.png")
#>>> 
