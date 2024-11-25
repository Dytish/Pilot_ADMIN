from rest_framework import serializers

class FlexibleModelSerializer(serializers.ModelSerializer):
    """
    Сериализатор, который включает все поля модели по умолчанию, но позволяет исключать указанные поля.
    """
    def __init__(self, *args, **kwargs):
        exclude = kwargs.pop('exclude', None)
        super().__init__(*args, **kwargs)
        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name, None)
