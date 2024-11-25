from django.core.management.base import BaseCommand
import json
from cbs.models import District, Region, City

class Command(BaseCommand):
    help = "Заполнение таблиц District, Region и City данными"

    def handle(self, *args, **kwargs):
        with open('cbs/data/data_sql.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for district_name in data['districts']:
            District.objects.get_or_create(name=district_name)

        for region in data['regions']:
            Region.objects.get_or_create(name=region['name'], district_id=region['district_id'])

        for city in data['cities']:
            City.objects.get_or_create(name=city['name'], region_id=city['region_id'])

        self.stdout.write(self.style.SUCCESS("Таблицы успешно заполнены!"))