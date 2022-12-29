from django.db import models

# Create your models here.
class TwitterUser(models.Model):
    id_str = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    screen_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True)
    profile_location = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    protected = models.CharField(max_length=255)
    followers_count = models.IntegerField()
    friends_count = models.IntegerField()
    statuses_count = models.IntegerField()
    lang = models.CharField(max_length=255, null=True)
    profile_image_url = models.CharField(max_length=255, null=True)
    profile_image_url_https = models.CharField(max_length=255, null=True)