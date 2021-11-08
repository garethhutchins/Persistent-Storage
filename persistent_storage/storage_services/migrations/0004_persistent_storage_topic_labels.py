# Generated by Django 3.2.9 on 2021-11-08 21:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage_services', '0003_alter_persistent_storage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='persistent_storage',
            name='topic_labels',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True),
        ),
    ]
