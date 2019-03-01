# Generated by Django 2.0.13 on 2019-03-01 13:41

import autoslug.fields
import courselib.json_fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coredata', '0022_add_new_visit_data'),
        ('advisornotes', '0006_on_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorVisitCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('hidden', models.BooleanField(default=False, editable=False)),
                ('config', courselib.json_fields.JSONField(default=dict, editable=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='autoslug', unique=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coredata.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='advisorvisit',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advisorvisit',
            name='version',
            field=models.PositiveSmallIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='advisorvisit',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='advisornotes.AdvisorVisitCategory'),
        ),
    ]
