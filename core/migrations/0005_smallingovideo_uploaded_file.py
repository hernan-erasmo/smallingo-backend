# Generated by Django 5.0.3 on 2024-03-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240308_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='smallingovideo',
            name='uploaded_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
