# Generated by Django 2.2.13 on 2020-06-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0052_auto_20200617_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]