# Generated by Django 3.1.2 on 2020-11-02 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swift_realtys', '0008_auto_20201030_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='text',
        ),
    ]