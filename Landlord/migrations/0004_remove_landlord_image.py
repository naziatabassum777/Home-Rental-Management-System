# Generated by Django 3.1.1 on 2020-09-29 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Landlord', '0003_landlord_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landlord',
            name='image',
        ),
    ]
