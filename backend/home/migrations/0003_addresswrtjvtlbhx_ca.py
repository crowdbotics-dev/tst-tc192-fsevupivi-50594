# Generated by Django 2.2.28 on 2022-12-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addresswrtjvtlbhx'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresswrtjvtlbhx',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
