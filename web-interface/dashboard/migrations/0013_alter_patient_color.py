# Generated by Django 3.2 on 2022-12-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_patient_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='color',
            field=models.IntegerField(default=1),
        ),
    ]
