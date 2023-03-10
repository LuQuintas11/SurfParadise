# Generated by Django 3.2 on 2023-01-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("full_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("contact_number", models.CharField(max_length=20)),
                ("order_number", models.CharField(blank=True, max_length=50)),
                ("message", models.TextField(max_length=300)),
            ],
            options={
                "verbose_name_plural": "Customer Enquiries",
            },
        ),
    ]
