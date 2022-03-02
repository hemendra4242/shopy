# Generated by Django 3.2.3 on 2022-03-01 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheaptechguys', '0005_product_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(default='Del', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(default='Del', null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
