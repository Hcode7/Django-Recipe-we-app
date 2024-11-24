from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='media/')
    ratings = GenericRelation(Rating)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} Comment on {self.recipe}'