# Generated by Django 4.2.1 on 2023-06-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_booking_delete_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='remark',
            field=models.TextField(null=True),
        ),
    ]
