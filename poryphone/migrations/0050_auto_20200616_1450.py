# Generated by Django 2.2.13 on 2020-06-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0049_auto_20200616_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='res1',
            new_name='sdef1',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='res100',
            new_name='sdef100',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='res30',
            new_name='sdef30',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='res45',
            new_name='sdef45',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='satk1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='satk100',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='satk30',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='satk45',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
