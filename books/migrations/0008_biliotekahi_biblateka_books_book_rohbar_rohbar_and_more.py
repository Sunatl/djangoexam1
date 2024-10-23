# Generated by Django 5.0 on 2024-10-23 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_student_suporidansh'),
    ]

    operations = [
        migrations.AddField(
            model_name='biliotekahi',
            name='biblateka',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.register'),
        ),
        migrations.AddField(
            model_name='books',
            name='book',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.biliotekahi'),
        ),
        migrations.AddField(
            model_name='rohbar',
            name='rohbar',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.register'),
        ),
        migrations.AddField(
            model_name='student',
            name='student',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.rohbar'),
        ),
    ]
