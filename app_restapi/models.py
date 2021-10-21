from django.db import models
from uuid import uuid4

# Create your models here.
from django.db.models import Index

from app_restapi.utlis import send_email


def save_logs(sending):
    LogEmail.objects.create()

class GuardObjectEvent(models.Model):
    """ таблица событий объекта"""
    class TypeChoises(models.TextChoices):
        FIRE = 'fire', 'Пожарная сработка'
        SERVICE = 'service', 'Техническое обслуживание'
        FAULT = 'fault', 'Неисправность устройства'

    id = models.BigAutoField(primary_key=True, db_index=True )
    uuid = models.UUIDField()
    rel_object_uuid = models.UUIDField()
    datetime = models.DateTimeField()
    type = models.CharField(max_length=100, choices=TypeChoises.choices)
    description = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        """ отравляем письмо, и записываем результат отправки в лог"""
        super().save(*args, **kwargs)
        recipients_list = []
        _object = GuardObject.objects.get(uuid=self.rel_object_uuid)
        names = GuardObjectUser.objects.filter(property__objectId__contains=[f'{_object.uuid}'])
        for name in names:
            email = name.property['email']
            name_user = name.property['name']
            recipients_list.append(name.property['email'])
            sending = send_email(name_user, _object.name, self.description, self.datetime, [f'{email}'])
            if sending:
                LogEmail.objects.create(
                    email=email,
                    description=GuardObjectEvent.objects.get(id=self.id),
                    object_name=_object,
                    name=GuardObjectUser.objects.get(id=name.id),
                    datetime=self.datetime,
                    type_sending_email=True,
                )
                print('успешно отправили')
            else:
                LogEmail.objects.create(
                    email=email,
                    description=GuardObjectEvent.objects.get(id=self.id),
                    object_name=_object,
                    name=GuardObjectUser.objects.get(id=name.id),
                    datetime=self.datetime,
                    type_sending_email=False,
                )
                print('ошибка в отправке')




class GuardObjectUser(models.Model):
    """ таблица пользователей """
    uuid = models.CharField(max_length=40)
    property = models.JSONField(null=True)


class GuardObject(models.Model):
    """ список объектов """
    id = models.BigAutoField(primary_key=True, db_index=True)
    uuid = models.UUIDField()
    name = models.CharField(max_length=300)


class LogEmail(models.Model):
    """ информация об отправленных письмах """
    email = models.EmailField(verbose_name='почта на которую отправленно событие')
    description = models.ForeignKey(GuardObjectEvent, on_delete=models.DO_NOTHING, verbose_name='событие на основании которого было отправленно письмо')
    object_name = models.ForeignKey(GuardObject, on_delete=models.DO_NOTHING, verbose_name='Событие на объекте')
    name = models.ForeignKey(GuardObjectUser, on_delete=models.DO_NOTHING, verbose_name='имя пользователя кому будет отправленно письмо')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата отправки письма')
    type_sending_email = models.BooleanField(verbose_name='Статус отправки письма')

