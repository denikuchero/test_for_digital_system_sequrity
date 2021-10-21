from django_filters import rest_framework
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *
# Create your views here.
# приложение должно иметь небольшое АPI со следующими методами:
# - метод для получение списка объектов



class ListGuardObject(viewsets.ReadOnlyModelViewSet):
    """метод для получение списка объектов
    метод для получение одного объекта """
    queryset = GuardObject.objects.all()
    serializer_class = ListGuardObjectSerialaizer


class ListEventObject(mixins.ListModelMixin,
                           GenericViewSet):
    """метод для получение списка событий объекта
    /api/v0/event/?rel_object_uuid=e3761ad4-f83c-4cba-a908-01f816ac48c0 """
    queryset = GuardObjectEvent.objects.all()
    serializer_class = ListEventObjectSerialaizer

    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = {
        'rel_object_uuid': ['exact'],
    }

class ReportEvent(mixins.ListModelMixin,
                           GenericViewSet):
    """
    генерирует отчет несколько типов отчетов за указанный промежуток времени (между
двумя датами)

    метод для выгрузки отчётов о событиях
    отчёт о событиях с одним переданным типом
(type=&quot;fire&quot;|type=&quot;service&quot;|type=&quot;fault&quot;), содержит следующую информацию

1) obj_name - название объекта
2) datetime - дата и время события
3) description - описание события

/api/v0/report-event/?type=fire&&datetime__gte=2019-01-01%2000:00:00
"""
    queryset = GuardObjectEvent.objects.all()
    serializer_class = ReportEventSerialaizer

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = {
        'datetime': ['gte', 'lte', 'exact'],
        'type': ['exact'],
    }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        list_serialaizer = []
        for item in serializer.data:
            try:
                # name = GuardObject.objects.get(uuid='59ba6709-18cd-4da2-b432-107346974231')
                # print(name.name)
                name = GuardObject.objects.get(uuid=item.pop('rel_object_uuid'))
                item['name'] = name.name
                list_serialaizer.append(item)

            except Exception as e:
                print(e)

        return Response(list_serialaizer)


class ReportSendSuccessSendEmail(mixins.ListModelMixin,
                           GenericViewSet):

    queryset = LogEmail.objects.filter(type_sending_email=True)
    serializer_class = ReportSendSuccessSendEmailSerialaizer

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = {
        'datetime': ['gte', 'lte', 'exact'],
    }


class ReportLogEmail(generics.ListAPIView):
    """ метод для выгрузки лога сервиса рассылок """
    queryset = LogEmail.objects.all()
    serializer_class = ReportSendSuccessSendEmailSerialaizer

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = {
        'datetime': ['gte', 'lte', 'exact'],
        'type_sending_email': ['exact'],
    }
