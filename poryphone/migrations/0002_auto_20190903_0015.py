# Generated by Django 2.2.4 on 2019-09-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='type',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='pokemon_type', to='poryphone.Type'),
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='weakness',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weakness',
            field=models.ManyToManyField(blank=True, related_name='pokemon_weakness', to='poryphone.Type'),
        ),
    ]
