# Generated by Django 2.1.1 on 2021-05-26 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djoba', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('reason', models.TextField()),
                ('date_created', models.DateField()),
                ('date_ended', models.DateField()),
                ('date_modified', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='job_search',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='djoba.JobSearch'),
            preserve_default=False,
        ),
    ]
