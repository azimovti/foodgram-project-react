from rest_framework import viewsets, status

from django.shortcuts import get_object_or_404
from .models import Recipe, RecipeSerializer
from rest_framework.response import Response

from api.permissions import IsAdminAuthorOrReadOnly


class RecipeViewSet(viewsets.ModelViewSet):
    """CRUD рецепты. """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAdminAuthorOrReadOnly)

    def adding_shoping_list(self, model, user, pk, name):
        """Добавление рецепта в список покупок."""
        recipe = get_object_or_404(Recipe, pk=pk)
        relation = model.objects.filter(user=user, recipe=recipe)
        if relation.exists():
            return Response(
                {'errors': 'Рецепт уже добавлен.'},
                status=status.HTTP_400_BAD_REQUEST)
        model.objects.create(user=user, recipe=recipe)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_shoping_list(self, model, user, pk, name):
        """"Удаление рецепта из списка покупок. """
        recipe = get_object_or_404(Recipe, pk=pk)
        relation = model.objects.filter(user=user, recipe=recipe)
        if not relation.exists():
            return Response(
                {'errors': 'Такой рецепт не существует. '},
                status=status.HTTP_400_BAD_REQUEST)
        relation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
