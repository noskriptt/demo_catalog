from django.db import models


class ImageAttributes(models.Model):
    # image attributes name,desc,date of creation
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    date_creation = models.DateField()


class Image(models.Model):
    # base model image
    image = models.ImageField(upload_to='images')
    attributes = models.ForeignKey(ImageAttributes, on_delete=models.CASCADE)
