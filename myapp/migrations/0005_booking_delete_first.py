# Generated by Django 4.2.1 on 2023-06-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_first_date_alter_first_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_address', models.CharField(max_length=200)),
                ('drop_address', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('altmobile', models.IntegerField()),
                ('gst', models.CharField(max_length=100)),
                ('remark', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='First',
        ),
    ]