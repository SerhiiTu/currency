# Generated by Django 4.2.7 on 2023-12-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_source_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='logo',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
