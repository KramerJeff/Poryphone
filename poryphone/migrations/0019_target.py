# Generated by Django 2.2.4 on 2019-11-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0018_delete_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
