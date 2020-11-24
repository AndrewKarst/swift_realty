# Generated by Django 3.2 on 2020-11-03 22:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swift_realtys', '0011_alter_listing_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='favorite',
            field=models.ManyToManyField(blank=True, default='1', related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
