# Generated by Django 2.2 on 2019-04-04 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Phone',
            new_name='phone',
        ),
    ]
