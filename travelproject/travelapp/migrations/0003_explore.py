# Generated by Django 4.0.4 on 2022-06-06 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='explore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField()),
            ],
        ),
    ]
