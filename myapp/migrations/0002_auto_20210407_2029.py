# Generated by Django 3.2 on 2021-04-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
