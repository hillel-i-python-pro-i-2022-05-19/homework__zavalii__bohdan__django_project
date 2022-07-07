# Generated by Django 4.0.5 on 2022-06-28 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0004_delete_contactdetails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday_date',
            field=models.CharField(default='2022-06-28 20:37:31.334704',
                                   help_text='Please enter data in the following format DD-MM-YY',
                                   max_length=100,
                                   verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_value',
            field=models.CharField(blank=True,
                                   help_text='The contact person phone number',
                                   max_length=17, validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                        regex='^\\+?1?\\d{9,15}$')],
                                   verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tags',
            field=models.CharField(
                choices=[('family', '#family'), ('friends', '#friends'),
                         ('trip', '#trip_to_planet_c-137')], default='family',
                help_text="Contact's personalized tags", max_length=50,
                verbose_name='Tags'),
        ),
    ]