# Generated by Django 3.0.3 on 2020-02-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_slider_url_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]