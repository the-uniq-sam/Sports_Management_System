# Generated by Django 3.1 on 2020-11-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('organiser', models.CharField(max_length=100)),
                ('about', models.TextField(default='')),
                ('rules', models.TextField(default='')),
                ('csvfile', models.FileField(upload_to='csvfile_for_guest/')),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_for_event', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('motto', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField()),
                ('rule1', models.TextField(default='')),
                ('rule2', models.TextField(default='')),
                ('rule3', models.TextField(default='')),
                ('rule4', models.TextField(default='')),
                ('rule5', models.TextField(default='')),
            ],
        ),
    ]
