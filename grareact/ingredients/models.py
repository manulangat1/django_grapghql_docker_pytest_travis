from django.db import models

# Create your models here.

class Category(models.Model):
    name  = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name