# Generated by Django 4.1.5 on 2023-02-09 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_alter_promocoes_data_publicacao"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="promocoes",
            name="data_publicacao",
        ),
    ]