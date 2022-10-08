# Generated by Django 4.0.4 on 2022-07-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_destination_delete_newplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='date',
            field=models.PositiveIntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='day',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
