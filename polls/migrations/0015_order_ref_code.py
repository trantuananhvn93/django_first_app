# Generated by Django 3.0 on 2019-12-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
