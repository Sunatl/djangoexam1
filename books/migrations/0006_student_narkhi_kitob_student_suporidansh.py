# Generated by Django 5.0 on 2024-10-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='narkhi_kitob',
            field=models.CharField(default=150, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='suporidansh',
            field=models.CharField(default=True, max_length=50),
        ),
    ]