# Generated by Django 3.1.2 on 2020-10-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pushup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockvalue',
            name='value',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
