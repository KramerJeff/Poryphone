# Generated by Django 2.2.4 on 2019-11-03 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0023_auto_20191102_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syncpair',
            name='trainer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='syncpair', to='poryphone.Trainer'),
        ),
    ]
