# Generated by Django 5.0.2 on 2024-03-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_item_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=30, null=True),
        ),
    ]