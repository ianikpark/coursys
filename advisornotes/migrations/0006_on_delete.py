# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 17:09
from __future__ import unicode_literals

import advisornotes.models
import autoslug.fields
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advisornotes', '0005_autoslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisornote',
            name='advisor',
            field=models.ForeignKey(editable=False, help_text='The advisor that created the note', on_delete=django.db.models.deletion.PROTECT, related_name='advisor', to='coredata.Person'),
        ),
        migrations.AlterField(
            model_name='advisornote',
            name='file_attachment',
            field=models.FileField(blank=True, max_length=500, null=True, storage=django.core.files.storage.FileSystemStorage(base_url=None, location='submitted_files'), upload_to=advisornotes.models.attachment_upload_to),
        ),
        migrations.AlterField(
            model_name='advisornote',
            name='nonstudent',
            field=models.ForeignKey(editable=False, help_text='The non-student that the note is about', null=True, on_delete=django.db.models.deletion.PROTECT, to='advisornotes.NonStudent'),
        ),
        migrations.AlterField(
            model_name='advisornote',
            name='student',
            field=models.ForeignKey(editable=False, help_text='The student that the note is about', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student', to='coredata.Person'),
        ),
        migrations.AlterField(
            model_name='advisornote',
            name='text',
            field=models.TextField(help_text='Note about a student', verbose_name='Contents'),
        ),
        migrations.AlterField(
            model_name='advisornote',
            name='unit',
            field=models.ForeignKey(help_text='The academic unit that owns this note', on_delete=django.db.models.deletion.PROTECT, to='coredata.Unit'),
        ),
        migrations.AlterField(
            model_name='advisorvisit',
            name='advisor',
            field=models.ForeignKey(editable=False, help_text='The advisor that created the note', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='coredata.Person'),
        ),
        migrations.AlterField(
            model_name='advisorvisit',
            name='nonstudent',
            field=models.ForeignKey(blank=True, help_text='The non-student that visited', null=True, on_delete=django.db.models.deletion.PROTECT, to='advisornotes.NonStudent'),
        ),
        migrations.AlterField(
            model_name='advisorvisit',
            name='program',
            field=models.ForeignKey(blank=True, help_text='The unit of the program the student is in', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='coredata.Unit'),
        ),
        migrations.AlterField(
            model_name='advisorvisit',
            name='student',
            field=models.ForeignKey(blank=True, help_text='The student that visited the advisor', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='coredata.Person'),
        ),
        migrations.AlterField(
            model_name='advisorvisit',
            name='unit',
            field=models.ForeignKey(help_text='The academic unit that owns this visit', on_delete=django.db.models.deletion.PROTECT, to='coredata.Unit'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='category',
            field=models.CharField(choices=[('INS', 'Institution'), ('PRO', 'Program'), ('OTH', 'Other')], max_length=3),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='name',
            field=models.CharField(help_text='The name of the artifact', max_length=140),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='autoslug', unique=True),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='unit',
            field=models.ForeignKey(help_text='The academic unit that owns this artifact', on_delete=django.db.models.deletion.PROTECT, to='coredata.Unit'),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='advisor',
            field=models.ForeignKey(editable=False, help_text='The advisor that created the note', on_delete=django.db.models.deletion.PROTECT, to='coredata.Person'),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='artifact',
            field=models.ForeignKey(blank=True, help_text='The artifact that the note is about', null=True, on_delete=django.db.models.deletion.PROTECT, to='advisornotes.Artifact'),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='best_before',
            field=models.DateField(blank=True, help_text='The effective date for this note', null=True),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='category',
            field=models.CharField(choices=[('EXC', 'Exceptions'), ('WAI', 'Waivers'), ('REQ', 'Requirements'), ('TRA', 'Transfers'), ('MIS', 'Miscellaneous')], max_length=3),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='course',
            field=models.ForeignKey(blank=True, help_text='The course that the note is about', null=True, on_delete=django.db.models.deletion.PROTECT, to='coredata.Course'),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='course_offering',
            field=models.ForeignKey(blank=True, help_text='The course offering that the note is about', null=True, on_delete=django.db.models.deletion.PROTECT, to='coredata.CourseOffering'),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='file_attachment',
            field=models.FileField(blank=True, max_length=500, null=True, storage=django.core.files.storage.FileSystemStorage(base_url=None, location='submitted_files'), upload_to=advisornotes.models.attachment_upload_to),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='text',
            field=models.TextField(help_text='Note about a student', verbose_name='Contents'),
        ),
        migrations.AlterField(
            model_name='artifactnote',
            name='unit',
            field=models.ForeignKey(help_text='The academic unit that owns this note', on_delete=django.db.models.deletion.PROTECT, to='coredata.Unit'),
        ),
        migrations.AlterField(
            model_name='nonstudent',
            name='email_address',
            field=models.EmailField(blank=True, help_text='Needed only if you want to copy the student on notes', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='nonstudent',
            name='notes',
            field=models.TextField(blank=True, help_text='Any general information for the student'),
        ),
        migrations.AlterField(
            model_name='nonstudent',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='autoslug', unique=True),
        ),
        migrations.AlterField(
            model_name='nonstudent',
            name='start_year',
            field=models.IntegerField(blank=True, help_text='The predicted/potential start year', null=True),
        ),
        migrations.AlterField(
            model_name='nonstudent',
            name='unit',
            field=models.ForeignKey(blank=True, help_text='The potential academic unit for the student', null=True, on_delete=django.db.models.deletion.PROTECT, to='coredata.Unit'),
        ),
    ]