# Generated by Django 3.2.3 on 2022-03-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheaptechguys', '0004_auto_20220301_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.FloatField(default=None, null=True),
        ),
    ]
