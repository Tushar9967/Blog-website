# Generated by Django 3.0.7 on 2021-07-13 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_newpost_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='newpost',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
