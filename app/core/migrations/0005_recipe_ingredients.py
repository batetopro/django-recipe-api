# Generated by Django 3.2.25 on 2024-03-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='core.Ingredient'),
        ),
    ]
