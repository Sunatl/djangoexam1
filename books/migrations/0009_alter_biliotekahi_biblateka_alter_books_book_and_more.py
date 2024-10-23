# Generated by Django 5.0 on 2024-10-23 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_biliotekahi_biblateka_books_book_rohbar_rohbar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biliotekahi',
            name='biblateka',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.register'),
        ),
        migrations.AlterField(
            model_name='books',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.biliotekahi'),
        ),
        migrations.AlterField(
            model_name='rohbar',
            name='rohbar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.register'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.rohbar'),
        ),
    ]