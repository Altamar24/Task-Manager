from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс User расширение стандартной модели пользователя Django,
    AbstractUser. Расширение дает возможность добавление фото пользователя
    """
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
