# Generated by Django 5.0.6 on 2024-06-10 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_invetory_survivor_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Invetory',
        ),
        migrations.AddField(
            model_name='survivor',
            name='infected',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survivor',
            name='is_infected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='survivor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.survivor'),
        ),
    ]
