# Generated by Django 2.2.4 on 2019-11-05 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0031_auto_20191104_2303'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='syncpairmove',
            unique_together={('move', 'syncpair')},
        ),
    ]
