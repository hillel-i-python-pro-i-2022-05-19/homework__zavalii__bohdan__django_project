# Generated by Django 4.0.5 on 2022-06-30 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0010_alter_contact_birthday_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactdetailsoptions",
            name="email_address",
            field=models.EmailField(
                blank=True,
                default="example@gmail.com",
                help_text="It is the email address of the person",
                max_length=254,
                verbose_name="Email",
            ),
        ),
        migrations.AlterField(
            model_name="contactdetailsoptions",
            name="linkedin_profile",
            field=models.CharField(
                blank=True,
                help_text="Here is the link to contact's LinkedIn profile",
                max_length=500,
                verbose_name="LinkedIn",
            ),
        ),
        migrations.AlterField(
            model_name="contactdetailsoptions",
            name="telegram_nickname",
            field=models.CharField(
                blank=True, help_text="Here is contact's telegram", max_length=100, verbose_name="Telegram"
            ),
        ),
    ]
