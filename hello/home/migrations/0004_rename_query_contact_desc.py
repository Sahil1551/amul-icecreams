# Generated by Django 3.2.6 on 2021-08-15 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='query',
            new_name='desc',
        ),
    ]
