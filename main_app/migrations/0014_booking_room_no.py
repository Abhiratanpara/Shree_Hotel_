# Generated by Django 4.2.7 on 2024-02-27 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_booking_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Room_No',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.room'),
            preserve_default=False,
        ),
    ]