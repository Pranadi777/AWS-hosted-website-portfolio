# Generated by Django 5.0.2 on 2024-03-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_item_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]