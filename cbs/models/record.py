from django.db import models
from cbs.models import user

# Create your models here.
class Record(models.Model):
    user_tg_id = models.OneToOneField(user.User, to_field="user_tg_id", on_delete=models.CASCADE, 
                                   verbose_name="Пользователь", related_name="records", db_column="user_tg_id")
    
    name = models.CharField(max_length=255, verbose_name="Имя пользователя", blank=True, null=True)  # Без дефолтного значения
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True, null=True)  # Без дефолтного значения
    location = models.JSONField(verbose_name="Локация", blank=True, null=True)  # Без дефолтного значения
    is_military = models.BooleanField(verbose_name="Состоит на военной службе", blank=True, null=True)  # Без дефолтного значения
    educational_goal = models.CharField(max_length=255, verbose_name="Образовательная цель", blank=True, null=True)  # Без дефолтного значения
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")  # Без дефолтного значения
    is_end = models.BooleanField(default=False, verbose_name="Завершено")  # С дефолтным значением
    is_completed = models.BooleanField(default=False, verbose_name="Обучение завершено")  # С дефолтным значением
    completion_comment = models.CharField(max_length=500, blank=True, null=True, verbose_name="Комментарий к обучению")  # Без дефолтного значения

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Удалено")


    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Record for {self.user_tg_id} - {self.name}"