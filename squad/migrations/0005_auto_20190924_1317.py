# Generated by Django 2.2.5 on 2019-09-24 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squad', '0004_auto_20190915_0924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'managed': False, 'ordering': ['-overall', 'age', '-value']},
        ),
    ]
