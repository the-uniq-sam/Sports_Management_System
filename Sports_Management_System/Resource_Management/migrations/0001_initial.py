# Generated by Django 3.1 on 2020-11-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('available', models.IntegerField(default=0)),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
    ]
