# Generated by Django 3.2 on 2023-03-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='Secure Blog', max_length=255),
        ),
    ]
