# Generated by Django 4.2.17 on 2025-04-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0063_alter_studentprofile_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
