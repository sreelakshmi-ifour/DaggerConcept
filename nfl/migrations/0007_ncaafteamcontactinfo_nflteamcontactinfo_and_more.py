# Generated by Django 4.2.4 on 2023-10-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0006_alter_contact_name_alter_depthchart_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NCAAFTeamContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Acronym', models.CharField(max_length=100)),
                ('Conference', models.CharField(max_length=100)),
                ('StadiumName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=10)),
                ('PostalCode', models.CharField(max_length=10)),
                ('Website', models.CharField(max_length=100)),
                ('Instagram', models.CharField(max_length=100)),
                ('Twitter', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NFLTeamContactInfo',
            fields=[
                ('ID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Mascot', models.CharField(max_length=100)),
                ('Conference', models.CharField(max_length=100)),
                ('StadiumName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=10)),
                ('PostalCode', models.CharField(max_length=10)),
                ('Website', models.CharField(max_length=100)),
                ('Instagram', models.CharField(max_length=100)),
                ('Twitter', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='playerdetail',
            options={'ordering': ['-Name']},
        ),
        migrations.AlterModelOptions(
            name='stadium',
            options={'ordering': ['-Name']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-Name']},
        ),
        migrations.AddIndex(
            model_name='playerdetail',
            index=models.Index(fields=['-Name'], name='nfl_playerd_Name_5f081e_idx'),
        ),
        migrations.AddIndex(
            model_name='stadium',
            index=models.Index(fields=['-Name'], name='nfl_stadium_Name_e3e749_idx'),
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['-Name'], name='nfl_team_Name_a96ebf_idx'),
        ),
    ]