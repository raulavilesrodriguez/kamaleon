# Generated by Django 3.2.9 on 2021-11-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamaleon', '0003_auto_20211124_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='compras',
            field=models.ManyToManyField(blank=True, related_name='sales', to='kamaleon.Compras'),
        ),
    ]
