# Generated by Django 3.0.6 on 2020-05-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200513_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
