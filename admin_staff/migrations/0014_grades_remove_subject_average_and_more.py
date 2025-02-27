# Generated by Django 5.1.3 on 2024-11-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0013_remove_studentprofile_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_grade_firstQ', models.IntegerField(blank=True, null=True)),
                ('subject_grade_secondQ', models.IntegerField(blank=True, null=True)),
                ('subject_grade_thirdQ', models.IntegerField(blank=True, null=True)),
                ('subject_grade_fourthQ', models.IntegerField(blank=True, null=True)),
                ('average', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='average',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_grade_firstQ',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_grade_fourthQ',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_grade_secondQ',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_grade_thirdQ',
        ),
    ]
