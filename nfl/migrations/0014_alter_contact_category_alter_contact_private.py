# Generated by Django 4.2.4 on 2023-11-16 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0013_testtable_remove_contact_contactlevel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Category',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Private',
            field=models.IntegerField(default=True),
        ),
    ]
