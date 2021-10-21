from django.core.mail import EmailMessage
from django.utils import timezone
from django.conf import settings


def send_email(name, object_name,description, datetime,
               recipients_list ):
    """отправка писема по наступившему событию """

    subject = 'Информация о событии'
    text_message = f'name={name}' \
                   f'object_name={object_name}' \
                   f'description={description}' \
                   f'datetime={datetime}' \
                   f''
    email = EmailMessage(
        subject,
        text_message,
        settings.EMAIL_FROM,
        recipients_list
    )
    email.content_subtype = 'html'
    result = email.send()

    return result

