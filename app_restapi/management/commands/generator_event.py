from random import randint, choice, choices, sample
from datetime import datetime
from uuid import uuid4

from django.core.management.base import BaseCommand

from app_restapi.models import GuardObject, GuardObjectEvent


class Command(BaseCommand):
    def handle(self, *args, **options):
        """генерация событий за текущую дату
        для записей из таблицы объектов генерирует событие с любым из доступных типов в
        рамках текущей даты
        - генерация должна происходить за текущую дату и время, для случайного
        количества объектов
        - событие содержит поля:
        1) uuid
        2) rel_object_uuid - объект для которого сгенерировано событие
        3) datetime - дата и время генерации события
        4) type - тип события (fire, service, fault)
        4) description - описание события (Пожарная сработка, Техническое
        обслуживание, Неисправность устройства)
        - бонусом покрытие сервиса тестами
        """
        limit_objects = GuardObject.objects.count()
        list_objects = [i for i in range(1, limit_objects+1)]
        type_dict = {'fire':'Пожарная сработк',
                'service': 'Техническое обслуживание',
                'fault': 'Неисправность устройства'}

        random_time_list = []
        for item in range(randint(1, limit_objects+1)):
            today_random_time = datetime.now().replace(hour=randint(0, 23), minute=randint(0, 59))
            random_time_list.append(today_random_time)

        dates = sorted(random_time_list)
        id_list = sample(list_objects, k=len(dates))
        print(id_list)

        for id, date in zip(id_list, dates):
            type_choise = choice(list(type_dict.keys()))
            _uuid = uuid4()
            rel_object_uuid = GuardObject.objects.get(id=id).uuid
            if type_choise == 'fire':
                type = GuardObjectEvent.TypeChoises.FIRE
            elif type_choise == 'service':
                type = GuardObjectEvent.TypeChoises.SERVICE
            else:
                type = GuardObjectEvent.TypeChoises.FAULT


            event = GuardObjectEvent.objects.create(
                                            id=GuardObjectEvent.objects.count()+1,
                                            uuid=_uuid,
                                            rel_object_uuid=rel_object_uuid,
                                            datetime=date,
                                            type=type,
                                            description = type_dict[type]
                                            )
            print(event)




