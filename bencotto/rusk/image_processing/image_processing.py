from os import makedirs
import os.path
import logging
import StringIO
from PIL import Image
from django.conf import settings
#from django.db.models import ImageField

#from django.core.files.uploadedfile import InMemoryUploadedFile
#from django.core.files.storage import default_storage
#from django.core.files.base import ContentFile

logger = logging.getLogger(__name__)

def getThumbFilename(imagePath, thumbSize):
    (root, ext) = os.path.splitext(imagePath)
    (x, y) = thumbSize
    return root + '_thumb' + format(x) + 'x' + format(y) + '.jpg'
    
def getThumbnail(imagePath):
    #raise NameError(imageField.name) rusks/1/images_logo_lg.gif
    THUMBNAIL_SIZE = (140, 140)
    thumbnailMediaPath = os.path.join(getThumbFilename(imagePath, THUMBNAIL_SIZE))
    image = Image.open(os.path.join(settings.MEDIA_ROOT, imagePath))
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    image.save(os.path.join(settings.MEDIA_ROOT, thumbnailMediaPath), "JPEG")
    return thumbnailMediaPath
    
#    
#def image_processing(ruskUserId, uploadedFile):
#    """
#    @todo: currently only snippets and not actually used; alternative used to generate the path dynamically using a callable
#    thumb creation shall be done lazy
#    @todo: create thumbnail
#    @todo: handle file already exists
#    """
#    mediaPath = os.path.join('rusks', str(ruskUserId), uploadedFile.name)
#    fullMediaPath = os.path.join(settings.MEDIA_ROOT, mediaPath)
#    if not os.path.exists(fullMediaPath):
#        os.makedirs(fullMediaPath)
#    #logger.debug('image_processing: {} => {}'.format(uploadedFile, targetPath))
#
#    #May be an in-memory file or file on disk
#    #content_type = uploadedFile.content_type #image/gif
#    inData = StringIO.StringIO(uploadedFile.read())
#
#    #Move into final destination
#    #Ipv hier direct weg t eschrijven zouden we het imageField moeten overschrijven met een andere locatie: HOE?
#    default_storage.save(mediaPath, ContentFile(inData.read()))
#
#    #Move the original
#    image = Image.open(inData);
#    #image = Image.open('/home/pbor/bencotto/bencotto/rusk/tests/data/test_image.gif');
#    #Image.open(StringIO("/home/blaine/Pictures/Me/neck-beard.jpg").read()) 
#    outData = StringIO.StringIO()
#    image.save(outData, format='JPEG')
#    
#    return InMemoryUploadedFile(outData, None, 'foo.jpg', 'image/jpeg', outData.len, None)
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
