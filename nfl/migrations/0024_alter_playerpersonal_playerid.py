# Generated by Django 4.2.4 on 2024-01-24 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0023_remove_playerpersonal_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerpersonal',
            name='PlayerID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nfl.playerdetail'),
        ),
    ]
