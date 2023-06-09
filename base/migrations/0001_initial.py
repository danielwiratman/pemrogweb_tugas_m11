# Generated by Django 4.1.7 on 2023-03-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FrictionSensor",
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
                ("value", models.FloatField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PowerSensor",
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
                ("value", models.FloatField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="TemperatureSensor",
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
                ("value", models.FloatField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
