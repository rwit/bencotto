from django.contrib import admin
from bencotto.rusk.models import *

class ruskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_added', 'views', 'image')
    #search_fields = ('')
    #list_filter =
    fields = ('user', 'title', 'description', 'image')
    #filter_horizontal = () for any n-to-n fields 

class likesAdmin(admin.ModelAdmin):
    list_display = ('user', 'rusk')
    #search_fields = ('')
    #list_filter =
    #fields = ('')
    #filter_horizontal = () for any n-to-n fields 
                 
class commentAdmin(admin.ModelAdmin):
    list_display = ('user', 'rusk', 'comment')
    #search_fields = ('')
    #list_filter =
    #fields = ('')
    #filter_horizontal = () for any n-to-n fields 
                 
admin.site.register(rusk, ruskAdmin)
admin.site.register(likes, likesAdmin)
admin.site.register(comments, commentAdmin)
