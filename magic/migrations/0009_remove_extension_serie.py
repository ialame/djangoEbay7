# Generated by Django 2.2.1 on 2019-05-12 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0008_remove_extension_tcgplayergroupid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extension',
            name='serie',
        ),
    ]
