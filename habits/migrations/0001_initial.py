# Generated by Django 4.2.6 on 2023-10-24 14:44

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
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, unique=True, verbose_name='место')),
            ],
            options={
                'verbose_name': 'место',
                'verbose_name_plural': 'места',
            },
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodicity', models.DurationField(default=datetime.timedelta(days=1), verbose_name='Периодичность')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=300, verbose_name='действие')),
                ('duration', models.PositiveIntegerField(verbose_name='Время на выполнение')),
                ('reward', models.CharField(blank=True, max_length=400, null=True, verbose_name='Вознаграждение')),
                ('is_pleasant', models.BooleanField(verbose_name='приятная привычка')),
                ('is_public', models.BooleanField(default=False, verbose_name='видна всем')),
                ('bound_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='habits.location', verbose_name='место')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]