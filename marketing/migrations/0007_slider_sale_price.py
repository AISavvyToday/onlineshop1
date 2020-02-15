# Generated by Django 3.0.3 on 2020-02-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0006_slider_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
