# Generated by Django 4.0.7 on 2023-07-03 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_bookowner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='follow',
        ),
        migrations.RenameField(
            model_name='userbooks',
            old_name='user',
            new_name='follow',
        ),
        migrations.RemoveField(
            model_name='book',
            name='bookOwner',
        ),
    ]