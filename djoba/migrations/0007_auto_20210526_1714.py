# Generated by Django 2.1.1 on 2021-05-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djoba', '0006_auto_20210526_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsearch',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10),
        ),
    ]
