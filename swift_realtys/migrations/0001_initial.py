# Generated by Django 3.1.2 on 2020-11-25 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=200)),
                ('phone_number', models.CharField(default='none', max_length=200)),
                ('email_address', models.EmailField(default='none', max_length=254)),
                ('agency', models.CharField(default='none', max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='realtor_photo')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'realtors',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='none', max_length=200)),
                ('num_bedrooms', models.IntegerField(default=0)),
                ('num_bathrooms', models.IntegerField(default=0)),
                ('description', models.CharField(default='none', max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(default='none', max_length=200)),
                ('favorite', models.ManyToManyField(blank=True, default='none', related_name='favorite', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'listings',
            },
        ),
    ]
