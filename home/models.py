from django.db import models
LABELS = (('hot','hot'),('new','new'),('','default'))
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=400)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=400, unique= True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)
    url = models.CharField(max_length=500, blank= True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)
    url = models.CharField(max_length=500, blank= True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media')
    slug = models.CharField(max_length=400, unique= True)   
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media')
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    size = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    specification = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    labels = models.CharField(choices= LABELS, max_length= 200, blank= True)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name