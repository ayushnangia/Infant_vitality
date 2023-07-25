# Generated by Django 3.2 on 2022-11-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20221112_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Others', 'OTHERS')], default='Male', max_length=6),
        ),
    ]
