# Generated by Django 5.1.1 on 2024-12-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0002_delete_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guests', models.PositiveIntegerField()),
                ('arrival_time', models.TimeField()),
                ('arrival_date', models.DateField()),
                ('specifications', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
