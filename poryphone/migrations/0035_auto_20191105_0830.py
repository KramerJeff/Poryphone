# Generated by Django 2.2.4 on 2019-11-05 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0034_auto_20191104_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemQuantity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='poryphone.Item')),
            ],
            options={
                'unique_together': {('item', 'quantity')},
            },
        ),
        migrations.DeleteModel(
            name='SyncPairMoveItem',
        ),
        migrations.AddField(
            model_name='syncpairmove',
            name='unlock_requirements',
            field=models.ManyToManyField(blank=True, null=True, related_name='items', to='poryphone.ItemQuantity'),
        ),
    ]