# Generated by Django 3.2.9 on 2021-11-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=255, null=True)),
                ('cost', models.CharField(blank=True, max_length=255, null=True)),
                ('prep_time', models.CharField(blank=True, max_length=255, null=True)),
                ('cook_time', models.CharField(blank=True, max_length=255, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('steps', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
