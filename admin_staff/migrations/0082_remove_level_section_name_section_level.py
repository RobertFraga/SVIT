# Generated by Django 4.2.17 on 2025-04-26 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0081_payment_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='section_name',
        ),
        migrations.AddField(
            model_name='section',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='admin_staff.level'),
        ),
    ]
