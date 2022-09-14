# Generated by Django 4.0.5 on 2022-09-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger_middleware', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlogger',
            name='counter',
            field=models.PositiveIntegerField(default=1, verbose_name='Counter'),
        ),
        migrations.AddField(
            model_name='requestlogger',
            name='method',
            field=models.CharField(default=1, max_length=20, verbose_name='HTTP Method'),
            preserve_default=False,
        ),
    ]