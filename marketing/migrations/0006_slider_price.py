# Generated by Django 3.0.3 on 2020-02-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_slider_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]