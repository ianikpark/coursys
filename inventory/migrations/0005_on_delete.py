# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 17:09
from __future__ import unicode_literals

import autoslug.fields
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_add_asset_attachments_and_change_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='category',
            field=models.CharField(blank=True, choices=[('EVEN', 'Events'), ('GEN', 'General'), ('OFF', 'Office Supplies'), ('BROC', 'Brochures'), ('BANN', 'Banners'), ('SWAG', 'Swag'), ('DISP', 'Display')], default='GEN', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='min_qty',
            field=models.PositiveIntegerField(blank=True, help_text='The minimum quantity that should be in stock before having to re-order', null=True, verbose_name='Minimum re-order quantity'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='min_vendor_qty',
            field=models.PositiveIntegerField(blank=True, help_text='The minimum quantity the vendor will let us order', null=True, verbose_name='Minimum vendor order quantity'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='qty_ordered',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Quantity on order'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='serial',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='autoslug', unique=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='tag',
            field=models.CharField(blank=True, help_text='SFU Asset Tag number, if it exists', max_length=60, null=True, verbose_name='Asset Tag Number'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='unit',
            field=models.ForeignKey(help_text='Unit to which this asset belongs', on_delete=django.db.models.deletion.PROTECT, to='coredata.Unit'),
        ),
        migrations.AlterField(
            model_name='assetchangerecord',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='records', to='inventory.Asset'),
        ),
        migrations.AlterField(
            model_name='assetchangerecord',
            name='event',
            field=models.ForeignKey(blank=True, help_text='The event it was for, if any', null=True, on_delete=django.db.models.deletion.PROTECT, to='outreach.OutreachEvent'),
        ),
        migrations.AlterField(
            model_name='assetchangerecord',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coredata.Person'),
        ),
        migrations.AlterField(
            model_name='assetchangerecord',
            name='qty',
            field=models.IntegerField(help_text="The change in quantity.  For removal of item, make it a negative number. For adding items, make it a positive.  e.g. '-2' if someone removed two ofthis item for something", verbose_name='Quantity adjustment'),
        ),
        migrations.AlterField(
            model_name='assetchangerecord',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='autoslug', unique=True),
        ),
        migrations.AlterField(
            model_name='assetdocumentattachment',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attachments', to='inventory.Asset'),
        ),
        migrations.AlterField(
            model_name='assetdocumentattachment',
            name='contents',
            field=models.FileField(max_length=500, storage=django.core.files.storage.FileSystemStorage(base_url=None, location='submitted_files'), upload_to=inventory.models.asset_attachment_upload_to),
        ),
        migrations.AlterField(
            model_name='assetdocumentattachment',
            name='created_by',
            field=models.ForeignKey(help_text='Document attachment created by.', on_delete=django.db.models.deletion.PROTECT, to='coredata.Person'),
        ),
        migrations.AlterField(
            model_name='assetdocumentattachment',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('asset',)),
        ),
    ]