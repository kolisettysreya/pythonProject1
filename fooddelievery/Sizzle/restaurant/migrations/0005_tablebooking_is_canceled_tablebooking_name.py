# Generated by Django 5.1.1 on 2024-12-07 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_tablebooking_email_tablebooking_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebooking',
            name='is_canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tablebooking',
            name='name',
            field=models.CharField(default='Default Name', max_length=255),
        ),
    ]
