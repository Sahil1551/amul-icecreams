# Generated by Django 3.2.6 on 2021-08-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_contact_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default=None, max_length=122),
        ),
    ]
