# Generated by Django 3.2.12 on 2022-03-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0008_alter_pollingunit_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
