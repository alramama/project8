# Generated by Django 4.0.5 on 2022-08-10 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_rename_bid_file_film_bid_doc_film_bid_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='bid_doc',
            new_name='bid_file',
        ),
        migrations.RemoveField(
            model_name='film',
            name='bid_info',
        ),
    ]
