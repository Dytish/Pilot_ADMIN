from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission

class Command(BaseCommand):
    help = 'Создает пользователя с ограниченными правами и делает его суперпользователем'

    def handle(self, *args, **kwargs):
        # Проверяем, существует ли пользователь
        if not User.objects.filter(username='cbs').exists():
            # Создаем пользователя
            user = User.objects.create_user(
                username='cbs',
                password='1111',
            )

            # Делаем пользователя суперпользователем
            user.is_superuser = True
            user.is_staff = True
            user.save()

            # Получаем разрешения только для моделей в вашем приложении (например, Cbs models)
            permissions = Permission.objects.filter(
                content_type__model__in=['record', 'user']  # Замените на свои модели
            )

            # Добавляем разрешения пользователю
            user.user_permissions.set(permissions)

            # Если у вас есть статус "персонаж", добавьте его сюда (пример):
            # user.profile.status = 'персонаж'  # Если у вас есть профиль, например, модель Profile
            # user.profile.save()

            self.stdout.write(self.style.SUCCESS('Пользователь cbs успешно создан с правами суперпользователя!'))
        else:
            self.stdout.write(self.style.SUCCESS('Пользователь cbs уже существует.'))
