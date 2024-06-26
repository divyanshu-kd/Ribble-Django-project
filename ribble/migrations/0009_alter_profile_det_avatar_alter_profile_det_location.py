# Generated by Django 4.2.7 on 2024-06-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ribble', '0008_alter_details_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_det',
            name='avatar',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='profile_det',
            name='location',
            field=models.TextField(default=None, max_length=250, null=True),
        ),
    ]
