# Generated by Django 2.2.1 on 2019-05-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0005_auto_20190512_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='tcgplayerGroupId',
            field=models.IntegerField(),
        ),
    ]