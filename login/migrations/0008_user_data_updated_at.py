# Generated by Django 3.2.9 on 2021-11-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_user_data_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
