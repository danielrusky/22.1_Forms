# Generated by Django 4.2.9 on 2024-01-07 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                ("version_number", models.IntegerField(verbose_name="номер версии")),
                (
                    "version_name",
                    models.CharField(max_length=50, verbose_name="название версии"),
                ),
                (
                    "is_current",
                    models.BooleanField(
                        default=False, verbose_name="признак текущаей версии"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]
