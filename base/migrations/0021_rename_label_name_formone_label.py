# Generated by Django 4.2.3 on 2023-08-29 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_rename_label_formone_label_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formone',
            old_name='label_name',
            new_name='label',
        ),
    ]
