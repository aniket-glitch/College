# Generated by Django 3.1.2 on 2020-10-20 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_auto_20201020_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='class_room_id',
            new_name='class_room',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='subject_id',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='teacher_id',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='classstudent',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='classstudent',
            old_name='class_id',
            new_name='subject_class',
        ),
        migrations.RenameField(
            model_name='studentcontact',
            old_name='student_id',
            new_name='student',
        ),
    ]