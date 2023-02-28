from django.db import models
from django.utils.text import slugify
# Create your models here.

class catagory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(catagory, self).save(*args, **kwargs)
        
class Menuitem(models.Model):
    title=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    catagory = models.ForeignKey(catagory, on_delete=models.PROTECT, default=1)


    