from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    """Класс Task используется для создания модели: 
    
    Attributes
    ----------
    title : CharField
        название задачи
    owner : ForeignKey
        автор задачи
    description : TextField
        описание задачи
    priority : SmallIntegerField
        приоритет задачи
    due_data : DateTimeField
        срок исполнения задачи
    completed : BooleanField
        галочка для отметки исполнения
    created_at : DateTimeField
        дата создания задачи
    updated_at : DateTimeField
        дата изменения задачи
    """
    title = models.CharField(max_length=50, verbose_name='Задача')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks', verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    LOW = 1
    MIDDLE = 2
    HIGH = 3
    STATUSES = (
        (LOW, 'Низкий'),
        (MIDDLE, 'Средний'),
        (HIGH, 'Высокий'),
    )
    priority = models.SmallIntegerField(
        default=LOW, choices=STATUSES, verbose_name='Приоритет')
    due_data = models.DateTimeField(
        default=datetime.now, verbose_name='Срок выполнения')
    completed = models.BooleanField(default=False, verbose_name='Исполнение')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
