# Generated by Django 2.0.1 on 2018-01-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaTree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='cohorts',
            field=models.ManyToManyField(to='adaTree.Cohort'),
        ),
    ]
