# Generated by Django 2.2.4 on 2019-11-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0020_move_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(blank=True, null=True, related_name='pokemon_move', to='poryphone.Move'),
        ),
    ]
