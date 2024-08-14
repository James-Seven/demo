# Generated by Django 5.0.7 on 2024-08-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='app.category'),
        ),
    ]
