# Generated by Django 2.1.3 on 2018-11-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinical_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientinfo',
            options={'verbose_name_plural': 'patientinfos'},
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='email',
            field=models.EmailField(max_length=70),
        ),
    ]
