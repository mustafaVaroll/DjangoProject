from django.contrib import admin
from .models import Movie

class  MovieAdmin(admin.ModelAdmin):
    list_display=('id','name','created_date')
    list_display_links=('id','name')
admin.site.register(Movie,MovieAdmin)
