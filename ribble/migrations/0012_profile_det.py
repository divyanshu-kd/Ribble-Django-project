# Generated by Django 4.2.7 on 2024-06-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ribble', '0011_delete_profile_det_details_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(default=None, max_length=250, null=True, upload_to='news/')),
                ('location', models.TextField(default=None, max_length=250, null=True)),
            ],
        ),
    ]
