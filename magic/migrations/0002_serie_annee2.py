# Generated by Django 2.2.1 on 2019-05-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='annee2',
            field=models.IntegerField(default=0),
        ),
    ]
