# Generated by Django 3.1.6 on 2022-09-21 10:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('suggestion', models.CharField(choices=[('KOREAN', '한식'), ('JAPANESE', '일식'), ('CHINESE', '중식'), ('ITALIAN', '양식'), ('SNACK', '분식')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='약속 제목', max_length=30)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 21, 19, 57, 59, 432859))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_appointment', to=settings.AUTH_USER_MODEL)),
                ('participate_user_set', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
