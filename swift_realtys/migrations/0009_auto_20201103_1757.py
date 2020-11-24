# Generated by Django 3.2 on 2020-11-03 17:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swift_realtys', '0008_realtor_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='favorite',
        ),
        migrations.AddField(
            model_name='listing',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
