# Generated by Django 4.2.17 on 2025-04-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0068_alter_studentprofile_have_form_138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='have_Form_138',
            field=models.BooleanField(default=False),
        ),
    ]
