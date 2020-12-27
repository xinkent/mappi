# Generated by Django 3.1.4 on 2020-12-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappi_app', '0002_auto_20201220_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='adress',
            new_name='store_adress',
        ),
        migrations.RemoveField(
            model_name='store',
            name='store_id',
        ),
        migrations.AddField(
            model_name='store',
            name='store_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='store',
            name='store_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
