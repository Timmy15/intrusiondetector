# Generated by Django 4.2.3 on 2023-08-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='john', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]