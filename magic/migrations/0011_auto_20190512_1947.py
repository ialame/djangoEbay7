# Generated by Django 2.2.1 on 2019-05-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0010_remove_extension_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extension',
            name='baseSetSize',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='block',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='boosterV3',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='code',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='codeV3',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='dateSortie',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='isFoilOnly',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='isOnlineOnly',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='keyruneCode',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='mcmId',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='mcmName',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='meta',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='mtgoCode',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='nbCartes',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='nomDossier',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='nomFR',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='nomRaccourci',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='nomUS',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='parentCode',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='releaseDate',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='totalSetSize',
        ),
        migrations.AlterField(
            model_name='extension',
            name='idPCA',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='extension',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
