# Generated by Django 2.1.5 on 2019-03-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunder', '0003_project_catagories'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='current_funds',
            field=models.IntegerField(default=0),
        ),
    ]
