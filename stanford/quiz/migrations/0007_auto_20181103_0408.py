# Generated by Django 2.1.2 on 2018-11-03 04:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20181103_0318'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_completed', models.DateTimeField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='max_time',
        ),
        migrations.AddField(
            model_name='category',
            name='max_time',
            field=models.DurationField(default=datetime.timedelta(0, 600)),
        ),
        migrations.AddField(
            model_name='categoryuserdata',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_data', to='quiz.Category'),
        ),
        migrations.AddField(
            model_name='categoryuserdata',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_data', to='quiz.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='categoryuserdata',
            unique_together={('category', 'student')},
        ),
    ]
