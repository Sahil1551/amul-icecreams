# Generated by Django 3.2.6 on 2022-06-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='add',
            field=models.TextField(max_length=150),
        ),
    ]
