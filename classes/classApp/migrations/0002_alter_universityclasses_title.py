# Generated by Django 4.0.6 on 2022-07-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityclasses',
            name='title',
            field=models.CharField(default='', max_length=60),
        ),
    ]
