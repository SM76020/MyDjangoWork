# Generated by Django 4.1.7 on 2023-03-28 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_details_contact_alter_details_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
