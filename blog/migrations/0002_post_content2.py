# Generated by Django 4.1.7 on 2023-02-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content2',
            field=models.TextField(blank=True),
        ),
    ]