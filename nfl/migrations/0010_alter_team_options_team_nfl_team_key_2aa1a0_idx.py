# Generated by Django 4.2.4 on 2023-11-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0009_alter_team_key_alter_team_teamid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-Key']},
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['-Key'], name='nfl_team_Key_2aa1a0_idx'),
        ),
    ]