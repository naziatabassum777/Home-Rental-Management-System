# Generated by Django 3.1.1 on 2020-09-29 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0005_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, default='images/thh.jpg', upload_to='images/Houes'),
        ),
    ]
