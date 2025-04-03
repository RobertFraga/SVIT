# Generated by Django 4.2.17 on 2025-04-03 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0070_alter_studentprofile_guardian_or_parent_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='choice_field',
            field=models.CharField(choices=[('Transfer_Out', 'Transfer_Out'), ('Transfer_In', 'Transfer_In'), ('Dropped', 'Dropped'), ('Late_Enrolee', 'Late_Enrolee'), ('CCT_Recipient', 'CCT_Recipient'), ('Balik_Aral', 'Balik_Aral'), ('Learner_with_Disability', 'Learner_with_Disability'), ('Accelerated', 'Accelerated')], default='Select Remarks', max_length=40),
        ),
    ]
