# Generated by Django 3.1.4 on 2020-12-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='issue',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='volume',
            field=models.CharField(max_length=50),
        ),
    ]
