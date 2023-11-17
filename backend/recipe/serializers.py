from rest_framework import serializers
from users.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Сериализатор для рецептов. """
    recipe = Recipe

    class Meta:
        model = Recipe
        fields = ('author', 'name', 'description', 'cooking_time', 'tags',
                  'ingredients')
