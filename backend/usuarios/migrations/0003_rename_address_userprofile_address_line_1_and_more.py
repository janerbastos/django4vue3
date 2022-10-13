# Generated by Django 4.0 on 2022-09-19 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address',
            new_name='address_line_1',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]