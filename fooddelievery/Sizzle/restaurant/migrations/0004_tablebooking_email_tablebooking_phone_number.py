# Generated by Django 5.1.1 on 2024-12-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebooking',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tablebooking',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]