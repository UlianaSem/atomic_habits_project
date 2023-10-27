# Generated by Django 4.2.6 on 2023-10-26 14:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('periodicity', models.PositiveIntegerField(default=1, verbose_name='Периодичность в днях')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=300, verbose_name='действие')),
                ('duration', models.PositiveIntegerField(verbose_name='Время на выполнение')),
                ('reward', models.CharField(blank=True, max_length=400, null=True, verbose_name='Вознаграждение')),
                ('is_pleasant', models.BooleanField(verbose_name='приятная привычка')),
                ('is_public', models.BooleanField(default=False, verbose_name='видна всем')),
                ('day', models.DateField(default=datetime.date.today, verbose_name='день выполнения')),
                ('bound_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='habits.location', verbose_name='место')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
