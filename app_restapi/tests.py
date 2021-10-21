from django.conf import settings
from django.core import mail
from django.test import TestCase
from datetime import datetime
from uuid import uuid4
from app_restapi.models import GuardObjectEvent
from app_restapi.utlis import send_email


class EmailTest(TestCase):
    def test_send_email(self):

        # Send message.
        name = 'Иванов Иван Иванович'
        object_name = uuid4()
        description = 'Неисправность устройства'
        _datetime = datetime.now()
        recipients_list = ['test@list.com']
        sending = send_email(name, object_name, description, _datetime, recipients_list)
        print(sending)


        mail.send_mail(
            'Subject here', 'Here is the message.',
            settings.EMAIL_FROM, ['to@example.com'],
            fail_silently=False,
        )

        self.assertEqual(sending, 1)
