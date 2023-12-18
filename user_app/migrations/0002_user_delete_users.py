# Generated by Django 5.0 on 2023-12-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=128)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Users",
        ),
    ]