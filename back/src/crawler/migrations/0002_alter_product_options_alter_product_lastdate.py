# Generated by Django 4.1 on 2022-10-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'type', 'price', 'shop', 'lastDate'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='lastDate',
            field=models.DateTimeField(verbose_name='Data do registro'),
        ),
    ]
