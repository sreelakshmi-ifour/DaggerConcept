# Generated by Django 4.2.4 on 2023-10-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0007_ncaafteamcontactinfo_nflteamcontactinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncaafteamcontactinfo',
            name='State',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nflteamcontactinfo',
            name='State',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]