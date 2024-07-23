# Generated by Django 5.0.7 on 2024-07-23 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mental', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='therapistprofile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='therapistprofile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
