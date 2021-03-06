# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-14 13:02


import autoslug.fields
import courselib.json_fields
from django.db import migrations, models
import django.db.models.deletion
import space.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=space.models.timezone_today)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('hidden', models.BooleanField(default=False, editable=False)),
                ('config', courselib.json_fields.JSONField(default=dict, editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'autoslug', unique=True)),
                ('last_modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='coredata.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(blank=True, choices=[(b'BRNBY', b'Burnaby Campus'), (b'SURRY', b'Surrey Campus'), (b'VANCR', b'Harbour Centre'), (b'OFFST', b'Off-campus'), (b'GNWC', b'Great Northern Way Campus'), (b'METRO', b'Other Locations in Vancouver')], max_length=5, null=True)),
                ('building', models.CharField(blank=True, choices=[(b'ASB', b'Applied Sciences Building'), (b'TASC1', b'TASC 1'), (b'SRY', b'Surrey'), (b'SEE', b'SEE Building'), (b'PTECH', b'Powertech'), (b'BLARD', b'Ballard'), (b'CC1', b'CC1'), (b'NTECH', b'NEUROTECH'), (b'SMH', b'SMH')], max_length=5, null=True)),
                ('floor', models.PositiveIntegerField(blank=True, null=True)),
                ('room_number', models.CharField(blank=True, max_length=25, null=True)),
                ('square_meters', models.DecimalField(decimal_places=2, max_digits=8)),
                ('infrastructure', models.CharField(blank=True, choices=[(b'WET', b'Wet Lab'), (b'DRY', b'Dry Lab'), (b'HPC', b'High-Performance Computing'), (b'STD', b'Standard')], max_length=3, null=True)),
                ('room_capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[(b'STAFF', b'Staff'), (b'FAC', b'Faculty'), (b'PDOC', b'Post-Doc'), (b'VISIT', b'Visitor'), (b'SESS', b'Sessional'), (b'LTERM', b'Limited-Term'), (b'TA', b'TA'), (b'GRAD', b'Grad Student'), (b'URA', b'URA')], max_length=5, null=True)),
                ('occupancy_count', models.PositiveIntegerField(blank=True, null=True)),
                ('own_or_lease', models.CharField(blank=True, choices=[(b'OWN', b'SFU Owned'), (b'LEASE', b'Leased')], max_length=5, null=True, verbose_name=b'SFU Owned or Leased')),
                ('comments', models.CharField(blank=True, max_length=400, null=True)),
                ('hidden', models.BooleanField(default=False, editable=False)),
                ('config', courselib.json_fields.JSONField(default=dict, editable=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'autoslug', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_description', models.CharField(help_text=b'e.g. "General Store"', max_length=256)),
                ('code', models.CharField(help_text=b'e.g. "STOR_GEN"', max_length=50)),
                ('COU_code_description', models.CharField(help_text=b'e.g. "Academic Office Support Space"', max_length=256)),
                ('COU_code_value', models.DecimalField(decimal_places=1, help_text=b'e.g. 10.1', max_digits=4)),
                ('hidden', models.BooleanField(default=False, editable=False)),
                ('config', courselib.json_fields.JSONField(default=dict, editable=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'autoslug', unique=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredata.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.RoomType'),
        ),
        migrations.AddField(
            model_name='location',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredata.Unit'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='space.Location'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='coredata.Person'),
        ),
    ]
