# Generated by Django 3.1.4 on 2020-12-31 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mappi_app', '0009_store_want_flag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='want_flag',
            new_name='went_flag',
        ),
    ]