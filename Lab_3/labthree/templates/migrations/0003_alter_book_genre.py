# Generated by Django 4.1.5 on 2023-01-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_remove_book_release_year_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('HORROR', 'Horror'), ('ROMANCE', 'Romance'), ('FANTASY', 'Fantasy'), ('SCIFI', 'Scifi'), ('EDCUCATION', 'Education'), ('OTHER', 'Other')], default='Other', max_length=20),
        ),
    ]