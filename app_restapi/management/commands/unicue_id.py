from random import randint, choice
from datetime import datetime
from uuid import uuid4

from django.core.management.base import BaseCommand

from app_restapi.models import GuardObject, GuardObjectEvent


class Command(BaseCommand):
    def handle(self, *args, **options):
        """ создает уникальные ключи в таблице"""
        event = GuardObjectEvent.objects.all().order_by('id')
        print(len(event))

        for index, item in enumerate(event):
            item.id = index+1
            item.save()
            print(index, item.id)