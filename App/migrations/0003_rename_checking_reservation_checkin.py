# Generated by Django 4.0.3 on 2022-04-21 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_rental_id_reservation_reservation_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='checking',
            new_name='checkin',
        ),
    ]
