# Generated by Django 2.0.6 on 2018-06-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amadon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cigars',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
