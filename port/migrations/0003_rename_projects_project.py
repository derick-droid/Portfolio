# Generated by Django 4.1.3 on 2022-11-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_projects_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]