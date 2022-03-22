# Generated by Django 3.2.12 on 2022-03-22 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastnmae', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('pollingunit_uniqueid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedLgaResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=10)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedPuResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_uniqueid', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('date_entered', models.DateField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedStateResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=11)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnouncedWardResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=11)),
                ('party_score', models.IntegerField()),
                ('entered_ny_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga_id', models.IntegerField()),
                ('lga_name', models.CharField(max_length=50)),
                ('state_id', models.IntegerField()),
                ('lga_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyid', models.CharField(max_length=4)),
                ('partynmae', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('uniquewardid', models.IntegerField(blank=True, null=True)),
                ('polling_unit_number', models.CharField(blank=True, max_length=50, null=True)),
                ('polling_unit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('long', models.CharField(blank=True, max_length=255, null=True)),
                ('entered_by_user', models.CharField(blank=True, max_length=50, null=True)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_id', models.IntegerField()),
                ('ward_name', models.CharField(max_length=50)),
                ('lga_id', models.IntegerField()),
                ('ward_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
    ]