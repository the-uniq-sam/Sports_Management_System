# Generated by Django 3.1.2 on 2020-11-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_remove_rule_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='event_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
