from django.db import models


class  Movie(models.Model):
    name=models.CharField(max_length=100,verbose_name='Film Adı')
    description=models.TextField(verbose_name='Film acıklaması')
    image=models.CharField(max_length=50,verbose_name='Film Resmi')
    created_date=models.DateTimeField(auto_now_add=True,verbose_name='Tarih')
    

    def __str__(self):
        return self.name
    
    def get_image_path(self):
        return '/img/' +self.image

