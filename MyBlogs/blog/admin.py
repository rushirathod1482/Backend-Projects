from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description','url','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','cat',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 50

    # class Media:
        # js = ("https://cdn.tiny.cloud/1/0ozr577uo9mv72du5lhmcmmb3ixzuidgf52q7eb3m6lxr334/tinymce/6/tinymce.min.js",'js/script.js',)
        # js = ("https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js",
        #       'js/script.js',)



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)