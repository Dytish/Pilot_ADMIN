from django.db import models


class User(models.Model):
    user_tg_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID пользователя")
    first_name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", blank=True, null=True)
    username = models.CharField(max_length=255, verbose_name="Telegram Username", blank=True, null=True)
    language_code = models.CharField(max_length=10, verbose_name="Язык интерфейса", blank=True, null=True)
    is_bot = models.BooleanField(default=False, verbose_name="Это бот")
    is_active = models.BooleanField(default=True, verbose_name="Активен в данный момент")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Удалено")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username or str(self.user_tg_id)