from django.conf import settings
from django import template
from bencotto.rusk.image_processing import image_processing

register = template.Library()

@register.simple_tag
def generateThumbnailSidebar(ruskImage):
    """custom tag to create the thumb (if not exists) and to generate the path to that image"""
    return image_processing.getThumbnail(ruskImage, settings.THUMBNAIL_SIDEBAR_SIZE)

@register.simple_tag
def generateThumbnailGrid(ruskImage):
    """custom tag to create the thumb (if not exists) and to generate the path to that image"""
    return image_processing.getThumbnail(ruskImage, settings.THUMBNAIL_GRID_SIZE)
