# Generated by Django 4.2.17 on 2025-04-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0046_remove_studentprofile_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='guardian_or_parent_mobile_number',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
