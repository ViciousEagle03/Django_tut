# Generated by Django 5.0 on 2023-12-29 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squareup', '0009_groupexpense_created_at_groupexpense_group_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='Grpname',
        ),
        migrations.RenameField(
            model_name='groupexpense',
            old_name='payer',
            new_name='participants',
        ),
    ]
