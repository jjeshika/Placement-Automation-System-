# Generated by Django 3.1.7 on 2021-05-09 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_invitedstudent'),
        ('quiz', '0002_quiz_quiz_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_for',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.job'),
        ),
    ]
