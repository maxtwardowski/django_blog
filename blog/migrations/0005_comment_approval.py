# Generated by Django 2.0.1 on 2018-02-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180216_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
