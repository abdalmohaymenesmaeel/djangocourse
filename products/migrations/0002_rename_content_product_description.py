# Generated by Django 4.1.7 on 2023-04-14 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="content", new_name="description",
        ),
    ]
