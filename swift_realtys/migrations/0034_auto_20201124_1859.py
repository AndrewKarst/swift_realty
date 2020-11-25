# Generated by Django 3.1.2 on 2020-11-24 23:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swift_realtys', '0033_merge_20201124_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='favorite',
            field=models.ManyToManyField(blank=True, default='none', related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='text',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='realtor_photo'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
