from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from cbs.models.user import User
from cbs.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get_object(self):
        """
        Переопределяем метод для поиска пользователя по user_tg_id вместо id.
        """
        id = self.kwargs.get('pk')  
        print(id)
        user_tg_id = self.kwargs.get('user_tg_id')  
        print(user_tg_id)
        try:
            return User.objects.get(user_tg_id=id) 
        except User.DoesNotExist:
            raise NotFound(f"Пользователь с Telegram ID {id} не найден.")
