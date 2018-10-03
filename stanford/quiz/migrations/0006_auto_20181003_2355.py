# Generated by Django 2.1.2 on 2018-10-03 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20181003_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='gvk_emri_demographics',
            name='internet_reliability',
            field=models.IntegerField(choices=[('COMP', 'Computer'), ('PHON', 'Smart Phone'), ('TABL', 'Tablet')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gvk_emri_demographics',
            name='leadership_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='gvk_emri_demographics',
            name='leadership_refresher',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gvk_emri_demographics',
            name='most_used_device',
            field=models.CharField(choices=[('COMP', 'Computer'), ('PHON', 'Smart Phone'), ('TABL', 'Tablet')], default='COMP', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gvk_emri_demographics',
            name='personal_device_hours',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gvk_emri_demographics',
            name='work_device_hours',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
