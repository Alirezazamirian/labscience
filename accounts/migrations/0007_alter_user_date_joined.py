# Generated by Django 5.0.6 on 2024-07-05 15:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
