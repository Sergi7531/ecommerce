# Generated by Django 4.2 on 2023-12-23 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0004_alter_sizing_size_short'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sizing',
            unique_together={('product', 'size_type', 'size_short')},
        ),
    ]
