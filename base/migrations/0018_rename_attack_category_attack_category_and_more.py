# Generated by Django 4.2.3 on 2023-08-23 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_formone_user_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attack',
            old_name='attack_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='attack_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='attack_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='attack_severity_level',
            new_name='severity_level',
        ),
        migrations.RemoveField(
            model_name='message',
            name='label',
        ),
        migrations.AlterField(
            model_name='message',
            name='attack_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.attack'),
        ),
    ]
