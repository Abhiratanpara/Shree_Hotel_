# Generated by Django 4.2.7 on 2023-11-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(default=None, max_length=500, null=True, upload_to='user_img/'),
        ),
    ]
