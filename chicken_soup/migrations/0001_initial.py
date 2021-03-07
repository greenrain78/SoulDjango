# Generated by Django 3.1.6 on 2021-03-07 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=30)),
                ('baekjoon_id', models.CharField(max_length=100, null=True, unique=True)),
                ('number', models.PositiveBigIntegerField(default=0)),
                ('email', models.CharField(max_length=200)),
                ('joined_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('birthday', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
