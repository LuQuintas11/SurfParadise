# Generated by Django 3.2 on 2023-01-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_alter_product_managers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="post",
            new_name="product",
        ),
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.IntegerField(default=3),
        ),
    ]
