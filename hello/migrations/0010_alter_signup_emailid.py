# Generated by Django 4.2.7 on 2024-03-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_alter_signup_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='EmailId',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]