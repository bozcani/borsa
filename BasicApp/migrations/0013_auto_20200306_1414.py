# Generated by Django 3.0.2 on 2020-03-06 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BasicApp', '0012_auto_20200306_1005'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CookieCrumbPair',
        ),
        migrations.RenameField(
            model_name='stockdatalastupdate',
            old_name='stock_market',
            new_name='stock',
        ),
    ]
