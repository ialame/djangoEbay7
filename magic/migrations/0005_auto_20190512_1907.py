# Generated by Django 2.2.1 on 2019-05-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0004_auto_20190512_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='tcgplayerGroupId',
            field=models.IntegerField(null=True),
        ),
    ]