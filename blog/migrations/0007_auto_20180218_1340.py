# Generated by Django 2.0.1 on 2018-02-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180217_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.CharField(max_length=100000),
        ),
    ]
