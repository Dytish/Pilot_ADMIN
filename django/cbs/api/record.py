from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status 
from cbs.models import Record
from cbs.serializers.record import RecordSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RecordSerializer

    def create(self, request, *args, **kwargs):
        """
        Метод для создания пользователя.
        """
        serializer = self.get_serializer(data=request.data, exclude=["is_completed", "completion_comment" ])  
        print(serializer)
        print(request.data)
        if serializer.is_valid():  
            print("dssssssssssssssss")
            self.perform_create(serializer)  
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        print("Ошибки сериализатора:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    @action(detail=False, methods=['get'], url_path='by-user-tg')
    def get_by_user_tg(self, request):
        """
        Поиск заявки по user_tg_id.
        """
        user_tg_id = request.query_params.get('user_tg_id')
        if not user_tg_id:
            return Response({"error": "Параметр 'user_tg_id' обязателен."}, status=400)
        try:
            user_tg_id = int(user_tg_id)
            records = Record.objects.filter(user_tg_id=user_tg_id)
            if not records.exists():
                return Response(serializer.data, status=200)
                return Response({"message": "Заявки не найдены."}, status=404)
            serializer = self.get_serializer(records, many=True)
            return Response(serializer.data, status=200)
        except ValueError:
            return Response({"error": "Параметр 'user_tg_id' должен быть целым числом."}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
