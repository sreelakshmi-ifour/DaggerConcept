# Generated by Django 4.2.4 on 2023-09-20 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('ContactType', models.IntegerField()),
                ('ContactLevel', models.IntegerField()),
                ('Owner', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Group', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='playerdetail',
            name='InjuryBodyPart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='playerdetail',
            name='InjuryNotes',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='playerdetail',
            name='InjuryPractice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='playerdetail',
            name='InjuryPracticeDescription',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='playerdetail',
            name='InjuryStatus',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='SubContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Primary', models.BooleanField()),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl.contact')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Number', models.CharField(max_length=20)),
                ('OwnerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl.subcontact')),
            ],
        ),
        migrations.CreateModel(
            name='OtherDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('OtherType', models.CharField(max_length=20)),
                ('Number', models.CharField(max_length=100)),
                ('OwnerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl.subcontact')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Line1', models.CharField(max_length=100)),
                ('Line2', models.CharField(blank=True, max_length=100, null=True)),
                ('Line3', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('PostalCode', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('OwnerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl.subcontact')),
            ],
        ),
    ]