# Generated by Django 4.0.3 on 2022-04-24 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_alter_reservation_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='created_at',
        ),
    ]
