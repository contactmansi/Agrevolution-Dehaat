# Generated by Django 2.1.3 on 2020-06-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dehaat_app', '0005_auto_20200614_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount_2015',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='amount_2016',
        ),
        migrations.AddField(
            model_name='transaction',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinput',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
