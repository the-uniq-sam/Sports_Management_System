# Generated by Django 3.1.2 on 2020-11-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20201113_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('motto', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('id_for_event', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='csvfile',
            field=models.FileField(upload_to='csvfile_for_guest/'),
        ),
    ]