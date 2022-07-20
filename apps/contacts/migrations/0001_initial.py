# Generated by Django 4.0.5 on 2022-06-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "contact_name",
                    models.CharField(help_text="It is the name of the person", max_length=200, verbose_name="Name"),
                ),
                (
                    "phone_value",
                    models.PositiveBigIntegerField(help_text="The person's phone number", verbose_name="Phone number"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
