from random import randint, choice
from datetime import datetime
from uuid import uuid4

from django.core.management.base import BaseCommand

from app_restapi.models import GuardObject, GuardObjectEvent, GuardObjectUser
from app_restapi.utlis import send_email


class Command(BaseCommand):
    def handle(self, *args, **options):
        name = ''
        object_name = ''
        description = ''
        datetime = ''
        recipients_list = ['test@list.com']

        sending = send_email(name, object_name, description, datetime, recipients_list)
        print(sending)
        if sending:
            print('отправка прошла успешно')
        else:
            print('не удалось отправить ')

