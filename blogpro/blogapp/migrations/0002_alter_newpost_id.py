# Generated by Django 3.2.3 on 2021-06-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
