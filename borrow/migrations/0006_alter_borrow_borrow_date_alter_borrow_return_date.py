# Generated by Django 4.0.7 on 2023-07-04 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0005_alter_borrow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
