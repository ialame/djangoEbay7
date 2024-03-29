# Generated by Django 2.2.1 on 2019-05-12 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0013_auto_20190512_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='baseSetSize',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='extension',
            name='nbCartes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='extension',
            name='nom',
            field=models.TextField(default=0, max_length=120),
        ),
        migrations.AddField(
            model_name='extension',
            name='nomDossier',
            field=models.TextField(default=0, max_length=120),
        ),
        migrations.AddField(
            model_name='extension',
            name='nomFR',
            field=models.TextField(default=0, max_length=120),
        ),
        migrations.AddField(
            model_name='extension',
            name='nomRaccourci',
            field=models.TextField(default=0, max_length=120),
        ),
        migrations.AddField(
            model_name='extension',
            name='nomUS',
            field=models.TextField(default=0, max_length=120),
        ),
    ]
