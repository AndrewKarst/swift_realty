# Generated by Django 3.2 on 2020-11-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swift_realtys', '0017_alter_listing_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
