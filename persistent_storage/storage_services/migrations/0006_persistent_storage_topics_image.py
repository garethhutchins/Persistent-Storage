# Generated by Django 3.2.9 on 2021-11-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_services', '0005_alter_persistent_storage_topic_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='persistent_storage',
            name='topics_image',
            field=models.FileField(default='', upload_to='models'),
        ),
    ]