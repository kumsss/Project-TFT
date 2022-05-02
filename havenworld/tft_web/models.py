from django.db import models
# Create your models here.
class Sermon(models.Model):
    title = models.CharField( max_length=20)
    audio = models.FileField( upload_to= 'sermons')
    thumbnail = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)
