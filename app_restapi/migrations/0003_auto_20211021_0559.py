# Generated by Django 3.2.8 on 2021-10-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restapi', '0002_auto_20211021_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardobject',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='guardobjectevent',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
