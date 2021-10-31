from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ('id','title', 'category', 'ingredients', 'description', "image", 'owner' )


