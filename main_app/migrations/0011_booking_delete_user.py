# Generated by Django 4.2.7 on 2024-02-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=12)),
                ('city', models.CharField(max_length=50)),
                ('adulte', models.IntegerField(max_length=5)),
                ('children', models.IntegerField(max_length=5)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
