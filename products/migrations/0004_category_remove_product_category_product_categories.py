# Generated by Django 4.1.7 on 2023-04-15 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_options_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(model_name="product", name="category",),
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.category",
            ),
        ),
    ]