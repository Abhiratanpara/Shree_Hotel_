# Generated by Django 4.2.7 on 2024-02-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_booking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.BigIntegerField(max_length=12),
        ),
    ]
