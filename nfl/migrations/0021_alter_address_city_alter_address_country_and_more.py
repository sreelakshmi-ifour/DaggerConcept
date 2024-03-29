# Generated by Django 4.2.4 on 2023-12-14 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0020_alter_ncaafplayer_globalteamid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='City',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='Country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='Line1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='PostalCode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='State',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='otherdetail',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='otherdetail',
            name='OtherType',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='otherdetail',
            name='Text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='Number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
