# Generated by Django 4.1.5 on 2023-02-09 01:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_remove_promocoes_data_publicacao"),
    ]

    operations = [
        migrations.AddField(
            model_name="promocoes",
            name="data_publicacao",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
