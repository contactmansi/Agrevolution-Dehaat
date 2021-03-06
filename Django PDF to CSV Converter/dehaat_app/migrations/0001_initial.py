# Generated by Django 2.1.3 on 2020-06-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalSheet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('particulars', models.CharField(max_length=100, unique=True)),
                ('amount_2015', models.CharField(max_length=15)),
                ('amount_2016', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_path', models.CharField(max_length=264)),
            ],
        ),
    ]
