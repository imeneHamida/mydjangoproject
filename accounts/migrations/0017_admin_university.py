# Generated by Django 4.2 on 2023-06-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_supervisor_email_alter_supervisor_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='university',
            field=models.CharField(max_length=100, null=True),
        ),
    ]