# Generated by Django 4.2.7 on 2024-03-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_rename_sex_signup_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='EmailId',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='EmailId_1',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
