# Generated by Django 3.1.1 on 2020-09-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landlord', '0002_auto_20200921_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='image',
            field=models.ImageField(blank=True, default='images/thh.jpg', null=True, upload_to='image/Landlord'),
        ),
    ]
