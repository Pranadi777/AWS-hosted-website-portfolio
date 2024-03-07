# Generated by Django 5.0.2 on 2024-03-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('template', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=50)),
                ('goal', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=500)),
                ('result', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=50)),
                ('items', models.ManyToManyField(blank=True, to='portfolio.item')),
            ],
        ),
    ]
