# Generated by Django 2.2.28 on 2023-08-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
