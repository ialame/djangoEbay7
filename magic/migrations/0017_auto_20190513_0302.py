# Generated by Django 2.2.1 on 2019-05-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0016_auto_20190513_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='mcmId',
            field=models.IntegerField(blank=True),
        ),
    ]
