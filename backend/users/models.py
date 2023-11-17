from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mail = models.EmailField(
        'Email',
        unique=True,
        max_length=20,
        null=False,
        help_text='Адрес электронной почты')
    username = models.CharField(
        'Имя пользователя',
        max_length=100,
        unique=True,
        null=False,
        help_text='Ваше имя для отображения на сайте')
    first_name = models.CharField(
        'Имя',
        null=False,
        max_length=100)
    last_name = models.CharField(
        'Фамилия', max_length=100)

    REQUIRED_FIELDS = ["mail"]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Follow(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'subscriber'],
                name='unique_user_and_subscriber'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.subscriber.username} подписан на {self.author.username}'
