# Generated by Django 2.1.3 on 2018-12-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20181221_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.CharField(max_length=50, null=True),
        ),
    ]