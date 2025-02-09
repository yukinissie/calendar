# Generated by Django 3.2.9 on 2021-11-24 18:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('user_subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(default='', max_length=100)),
                ('contents', models.CharField(blank=True, default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新日')),
                ('end', models.DateTimeField(default=datetime.datetime(2021, 11, 24, 18, 37, 8, 967243))),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarSite.subject')),
            ],
        ),
    ]
