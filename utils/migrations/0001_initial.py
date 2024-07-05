# Generated by Django 5.0.6 on 2024-07-05 16:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('is_answered', models.BooleanField(default=False, verbose_name='Is Answered')),
                ('type', models.CharField(choices=[('Problem', 'انتقادات'), ('Suggestion', 'پیشنهادات'), ('Error report', 'گزارش مشکل'), ('Contact us', 'ارتباط با ما')], max_length=40, verbose_name='Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
