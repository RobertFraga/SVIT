# Generated by Django 5.1.3 on 2024-11-26 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0010_accountingstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='grades',
            field=models.ManyToManyField(blank=True, null=True, to='admin_staff.subject'),
        ),
    ]