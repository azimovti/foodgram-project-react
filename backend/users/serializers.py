from rest_framework import serializers
from users.models import Follow


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""
#    user = serializers.SlugRelatedField(
#        slug_field='username', read_only=True,
#        default=serializers.CurrentUserDefault())
#    following = serializers.SlugRelatedField(slug_field='username',
#                                             queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('author', 'subscriber')

        validators = [serializers.UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message='Вы уже подписаны'
        )]
