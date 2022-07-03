from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tags(models.Model):
    label = models.CharField(max_length=255)


class TaggedItems(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    # Object has two attributes: 1. Type(Product, Video, Article, Tables), 2. ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
