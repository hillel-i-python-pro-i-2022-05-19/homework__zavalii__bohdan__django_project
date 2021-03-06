# Generated by Django 4.0.5 on 2022-06-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0009_contactdetailsoptions_alter_contact_birthday_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="birthday_date",
            field=models.DateField(
                blank=True, help_text="Please enter data in the following format %Y-%m-%d", verbose_name="Date of birth"
            ),
        ),
    ]
