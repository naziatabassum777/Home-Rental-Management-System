# Generated by Django 3.1.1 on 2020-10-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]