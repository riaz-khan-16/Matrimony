# Generated by Django 4.2.6 on 2023-10-17 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prposals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_id', models.CharField(max_length=80, null=True)),
                ('proposal_message', models.CharField(max_length=800, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
