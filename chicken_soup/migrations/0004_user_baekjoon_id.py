# Generated by Django 3.1.6 on 2021-03-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicken_soup', '0003_auto_20210305_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='baekjoon_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
