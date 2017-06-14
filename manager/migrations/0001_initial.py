# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 21:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField(default=200)),
                ('recurring', models.BooleanField(default=False)),
                ('reg_date', models.DateField(default=datetime.date.today)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('monthly_wage', models.IntegerField(default=25000)),
                ('lead', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='DevMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('role', models.CharField(max_length=64)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_made', models.DateField(default=datetime.date.today)),
                ('amount', models.IntegerField(default=500)),
                ('comment', models.CharField(max_length=100)),
                ('billable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='manager.Billable')),
            ],
            options={
                'ordering': ('billable_id',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('description', models.CharField(max_length=1000)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='manager.Client')),
                ('developers', models.ManyToManyField(through='manager.DevMembership', to='manager.Developer')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='manager.Developer')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='devmembership',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Project'),
        ),
        migrations.AddField(
            model_name='billable',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billables', to='manager.Developer'),
        ),
        migrations.AddField(
            model_name='billable',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billables', to='manager.Project'),
        ),
    ]
