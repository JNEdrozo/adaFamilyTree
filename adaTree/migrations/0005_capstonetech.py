# Generated by Django 2.0.1 on 2018-01-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaTree', '0004_internshipcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapstoneTech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
