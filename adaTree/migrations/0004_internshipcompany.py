# Generated by Django 2.0.1 on 2018-01-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaTree', '0003_instructor_pronouns'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
