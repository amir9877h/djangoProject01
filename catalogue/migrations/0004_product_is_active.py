# Generated by Django 4.2.9 on 2024-01-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0003_alter_category_options_alter_brand_parent_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
