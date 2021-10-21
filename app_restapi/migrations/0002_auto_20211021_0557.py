# Generated by Django 3.2.8 on 2021-10-21 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_restapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardobject',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='guardobjectevent',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='LogEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='почта на которую отправленно событие')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='дата отправки письма')),
                ('type_sending_email', models.BooleanField(verbose_name='Статус отправки письма')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_restapi.guardobjectevent', verbose_name='событие на основании которого было отправленно письмо')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_restapi.guardobjectuser', verbose_name='имя пользователя кому будет отправленно письмо')),
                ('object_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_restapi.guardobject', verbose_name='Событие на объекте')),
            ],
        ),
    ]