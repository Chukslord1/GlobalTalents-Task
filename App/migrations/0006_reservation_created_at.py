# Generated by Django 4.0.3 on 2022-04-22 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_reservation_rental_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 22, 10, 31, 2, 378422), null=True),
        ),
    ]
