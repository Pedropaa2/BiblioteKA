# Generated by Django 4.0.7 on 2023-07-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(choices=[('Bad', 'Bad'), ('Good', 'Good'), ('Very Good', 'Very Good')], max_length=20)),
                ('paperback', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('reviews', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
            ],
        ),
    ]
