# Generated by Django 2.1.2 on 2018-10-22 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181022_1211'),
        ('members', '0002_auto_20181018_1221'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]