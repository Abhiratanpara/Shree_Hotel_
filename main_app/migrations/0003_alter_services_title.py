# Generated by Django 4.2.7 on 2023-11-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
    ]