# Generated by Django 3.0 on 2019-12-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
