# Generated by Django 2.2 on 2020-02-24 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='labours',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='supervisor',
        ),
    ]