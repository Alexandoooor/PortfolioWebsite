from django.db import models

# Create your models here.
class RecentPosts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

class BannerImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.FilePathField(path="/images")
