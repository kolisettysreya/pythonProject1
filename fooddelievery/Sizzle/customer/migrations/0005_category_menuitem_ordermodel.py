# Generated by Django 5.1.1 on 2024-12-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_feedback_remove_category_delivery_mode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='menu_images/')),
                ('price', models.CharField(max_length=7)),
                ('category', models.ManyToManyField(related_name='item', to='customer.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(max_length=7)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('is_shipped', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='customer.menuitem')),
            ],
        ),
    ]
