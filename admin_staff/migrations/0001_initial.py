# Generated by Django 5.1.3 on 2024-11-18 06:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminStaff',
            fields=[
                ('admin_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=24, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'admin_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdmissionStaff',
            fields=[
                ('admission_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=10, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'admission_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GuidanceStaff',
            fields=[
                ('guidance_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=10, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'guidance_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistrarStaff',
            fields=[
                ('registrar_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=10, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'registrar_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announcement_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('event', models.DateField(null=True)),
            ],
            options={
                'db_table': 'annoucement',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(blank=True, max_length=30, null=True)),
                ('subject_discripiton', models.CharField(blank=True, max_length=30, null=True)),
                ('subject_grade_firstQ', models.IntegerField(blank=True, null=True)),
                ('subject_grade_secondQ', models.IntegerField(blank=True, null=True)),
                ('subject_grade_thirdQ', models.IntegerField(blank=True, null=True)),
                ('subject_grade_fourthQ', models.IntegerField(blank=True, null=True)),
                ('average', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=20)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.level')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyStaff',
            fields=[
                ('faculty_staff_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=10, null=True)),
                ('civil_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Status', max_length=10, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('birth_place', models.CharField(blank=True, max_length=200, null=True)),
                ('religion', models.CharField(blank=True, max_length=24, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('section', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.section')),
                ('subject', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.subject')),
            ],
            options={
                'db_table': 'faculty_staff',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('student_lrn', models.BigIntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=24, null=True)),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(blank=True, max_length=200, null=True)),
                ('religion', models.CharField(blank=True, max_length=24, null=True)),
                ('civil_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Status', max_length=10, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('adviser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.facultystaff')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.level')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.section')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student_profile',
                'managed': True,
            },
        ),
    ]
