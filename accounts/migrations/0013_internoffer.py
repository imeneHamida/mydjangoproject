# Generated by Django 4.2 on 2023-06-02 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_internshipapp_applicant'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, max_length=100, null=True)),
                ('companyName', models.CharField(blank=True, max_length=100, null=True)),
                ('companyAdrss', models.CharField(blank=True, max_length=100, null=True)),
                ('strtDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('Salary', models.IntegerField(blank=True, null=True)),
                ('internMaster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offerspr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
