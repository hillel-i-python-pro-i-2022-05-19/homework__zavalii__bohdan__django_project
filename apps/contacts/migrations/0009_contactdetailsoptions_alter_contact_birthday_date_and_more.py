# Generated by Django 4.0.5 on 2022-06-30 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0008_contact_tags_by_foreign_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetailsOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('email_address',
                 models.EmailField(default='example@gmail.com',
                                   help_text='It is the email address of the person',
                                   max_length=254, verbose_name='Email')),
                ('telegram_nickname',
                 models.CharField(help_text="Here is contact's telegram",
                                  max_length=100, verbose_name='Telegram')),
                ('linkedin_profile', models.CharField(
                    help_text="Here is the link to contact's LinkedIn profile",
                    max_length=500, verbose_name='LinkedIn')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday_date',
            field=models.DateField(
                help_text='Please enter data in the following format %Y-%m-%d',
                verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tags_by_foreign_key',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='contact_tags_related_by_foreign_key',
                                    to='contacts.tags'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_details_by_foreign_key',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='contacts.contactdetailsoptions'),
        ),
    ]