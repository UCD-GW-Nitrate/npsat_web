# Generated by Django 2.1.1 on 2019-01-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npsat_manager', '0003_auto_20190123_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b118basin',
            name='npsat_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='county',
            name='npsat_id',
            field=models.IntegerField(null=True),
        ),
    ]