from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    likes = models.TextField()
    owner = models.ForeignKey('users.User', related_name='recipes',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
