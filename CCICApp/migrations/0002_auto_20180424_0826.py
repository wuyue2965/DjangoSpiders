# Generated by Django 2.0.4 on 2018-04-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCICApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vvebo',
            name='comment',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='vvebo',
            name='device',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='vvebo',
            name='keyword',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='vvebo',
            name='time',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='vvebo',
            name='url',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='vvebo',
            name='user_id',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='vvebo',
            name='user_name',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
