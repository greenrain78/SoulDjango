# Generated by Django 3.1.6 on 2021-03-07 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chicken_soup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.IntegerField(default=0)),
                ('tier', models.CharField(default='unranked', max_length=50)),
                ('higher_rating', models.IntegerField(default=0)),
                ('class_rating', models.IntegerField(default=0)),
                ('solved_rating', models.IntegerField(default=0)),
                ('vote_count_rating', models.IntegerField(default=0)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chicken_soup.user')),
            ],
        ),
    ]
