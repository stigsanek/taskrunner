from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField('Описание', max_length=255)
    close_date = models.DateField('Дата завершения')
    is_complete = models.BooleanField('Выполнено', default=False)
    is_important = models.BooleanField('Важная', default=False)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
