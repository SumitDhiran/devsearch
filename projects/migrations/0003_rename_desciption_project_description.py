# Generated by Django 3.2.5 on 2021-08-10 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210808_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='desciption',
            new_name='description',
        ),
    ]
