# Generated by Django 5.0.2 on 2024-03-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_item_options_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='reference',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
