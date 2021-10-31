from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    image = models.TextField()
    likes = models.IntegerField()
    owner = models.ForeignKey('users.User', related_name='recipes', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
