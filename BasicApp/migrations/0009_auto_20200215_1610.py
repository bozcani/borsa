# Generated by Django 3.0.2 on 2020-02-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasicApp', '0008_auto_20200215_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(max_length=100),
        ),
    ]
