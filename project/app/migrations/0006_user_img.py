# Generated by Django 4.2.6 on 2024-01-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]