# Generated by Django 4.0.7 on 2023-07-03 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_marks', to='book.book')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='book',
            field=models.ManyToManyField(related_name='user_book', through='users.UserBooks', to='book.book'),
        ),
        migrations.AddField(
            model_name='userbooks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_marks', to=settings.AUTH_USER_MODEL),
        ),
    ]