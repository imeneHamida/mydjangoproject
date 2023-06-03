# Generated by Django 4.2 on 2023-06-02 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipapp',
            name='applicant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internship_app', to=settings.AUTH_USER_MODEL),
        ),
    ]