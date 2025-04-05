from django.db import models

# Create your models here.
class Receipe(models.Model):
    r_name = models.CharField(max_length=255)
    r_description = models.TextField()
    r_image = models.ImageField(upload_to="images")