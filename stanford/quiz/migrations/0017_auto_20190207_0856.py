# Generated by Django 2.1.3 on 2019-02-07 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20190206_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='practice_quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='practice_category', to='quiz.Quiz'),
        ),
    ]