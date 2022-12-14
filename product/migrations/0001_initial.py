# Generated by Django 3.2.15 on 2022-08-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gadgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Product Name')),
                ('brand', models.CharField(max_length=22, verbose_name='Product Brand')),
                ('price', models.FloatField()),
                ('qty', models.SmallIntegerField()),
                ('warranty', models.CharField(choices=[('international', 'International'), ('national', 'National'), ('domestic', 'Domestic')], max_length=21)),
                ('Home_delivery', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'prod',
            },
        ),
    ]
