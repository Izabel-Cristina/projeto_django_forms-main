# Generated by Django 4.1.5 on 2023-02-07 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Promocoes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("local", models.CharField(max_length=255)),
                ("titulo", models.CharField(max_length=255)),
                ("conteudo", models.TextField()),
                (
                    "data_publicacao",
                    models.DateTimeField(
                        verbose_name=datetime.datetime(
                            2023, 2, 7, 21, 55, 6, 536740, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "image_capa",
                    models.ImageField(blank=True, null=True, upload_to="static/home/"),
                ),
            ],
        ),
    ]
