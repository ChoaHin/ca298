# Generated by Django 4.1.5 on 2023-01-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0004_alter_mymodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='Title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]