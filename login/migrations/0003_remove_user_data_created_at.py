# Generated by Django 3.2.9 on 2021-11-18 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_data_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='created_at',
        ),
    ]
