# Generated by Django 2.2.1 on 2019-05-12 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0007_auto_20190512_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extension',
            name='tcgplayerGroupId',
        ),
    ]
