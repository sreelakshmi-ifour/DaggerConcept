# Generated by Django 4.2.4 on 2023-12-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0017_rename_number_otherdetail_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='NCAAFPlayer',
            fields=[
                ('PlayerID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(blank=True, max_length=100, null=True)),
                ('LastName', models.CharField(blank=True, max_length=100, null=True)),
                ('TeamID', models.CharField(blank=True, max_length=10, null=True)),
                ('Team', models.CharField(blank=True, max_length=100, null=True)),
                ('Jersey', models.CharField(blank=True, max_length=100, null=True)),
                ('Position', models.CharField(blank=True, max_length=100, null=True)),
                ('PositionCategory', models.CharField(blank=True, max_length=100, null=True)),
                ('Class', models.CharField(blank=True, max_length=100, null=True)),
                ('Height', models.CharField(blank=True, max_length=100, null=True)),
                ('Weight', models.CharField(blank=True, max_length=100, null=True)),
                ('BirthCity', models.CharField(blank=True, max_length=100, null=True)),
                ('BirthState', models.CharField(blank=True, max_length=100, null=True)),
                ('Updated', models.CharField(blank=True, max_length=100, null=True)),
                ('Created', models.CharField(blank=True, max_length=100, null=True)),
                ('GlobalTeamID', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NCAAFTeam',
            fields=[
                ('TeamID', models.AutoField(primary_key=True, serialize=False)),
                ('Key', models.CharField(blank=True, max_length=10, null=True)),
                ('Active', models.CharField(blank=True, max_length=100, null=True)),
                ('School', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('StadiumID', models.CharField(blank=True, max_length=100, null=True)),
                ('GlobalTeamID', models.CharField(blank=True, max_length=100, null=True)),
                ('TeamLogoUrl', models.CharField(blank=True, max_length=100, null=True)),
                ('ConferenceID', models.CharField(blank=True, max_length=100, null=True)),
                ('Conference', models.CharField(blank=True, max_length=100, null=True)),
                ('ShortDisplayName', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
