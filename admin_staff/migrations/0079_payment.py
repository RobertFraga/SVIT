# Generated by Django 4.2.17 on 2025-04-22 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0078_studentprofile_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('payment_type', models.CharField(blank=True, choices=[('option1', 'Credit/Debit Card Payment'), ('option2', 'Bank Transfer'), ('option3', 'Mobile Payment Apps'), ('option4', 'Office Transaction')], default='Status', max_length=50, null=True)),
                ('student_lrn', models.ForeignKey(db_column='student_lrn', on_delete=django.db.models.deletion.CASCADE, to='admin_staff.studentprofile')),
            ],
            options={
                'db_table': 'payment',
                'managed': True,
            },
        ),
    ]
