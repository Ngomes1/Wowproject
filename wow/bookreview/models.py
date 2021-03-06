from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    socialtag_id = models.AutoField(primary_key=True)    
class Post(models.Model):
    title = models.CharField(max_length=20)
    review = models.CharField(max_length=1000)
    img_link = models.URLField(max_length=1000)
    instagram = models.CharField(max_length=100, blank=True)
    meta = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    social = models.ManyToManyField(Tag)
    date_created = models.DateTimeField()
    post_id = models.AutoField(primary_key=True)
    genre_id = models.CharField(blank=True, max_length=100)
    
