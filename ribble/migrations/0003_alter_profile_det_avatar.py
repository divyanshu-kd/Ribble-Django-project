# Generated by Django 4.2.7 on 2024-06-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ribble', '0002_profile_det'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_det',
            name='avatar',
            field=models.ImageField(upload_to='C:/web_development/Python_backend_files/dribble/Static/'),
        ),
    ]