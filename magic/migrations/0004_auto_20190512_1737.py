# Generated by Django 2.2.1 on 2019-05-12 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0003_auto_20190512_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='serie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='magic.Serie'),
        ),
    ]