# Generated by Django 2.0.2 on 2018-02-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180222_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='index',
            field=models.IntegerField(auto_created=True, default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
