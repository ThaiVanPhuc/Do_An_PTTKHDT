# Generated by Django 4.2.4 on 2024-04-21 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='product',
        ),
    ]
