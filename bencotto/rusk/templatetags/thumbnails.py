from django import template
from bencotto.rusk.image_processing import image_processing

register = template.Library()

@register.simple_tag
def generateThumbnail(ruskImage):
    """custom tag to create the thumb (if not exists) and to generate the path to that image"""
    return image_processing.getThumbnail(ruskImage)
