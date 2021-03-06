# Generated by Django 3.1.7 on 2021-04-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_studentresume_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresume',
            name='branch',
            field=models.CharField(choices=[('CS', 'Computer Engineering'), ('IT', 'Information Technology'), ('AE', 'Automobile Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('CHE', 'Chemical Engineering'), ('EXTC', 'Electronics And Telecommunication'), ('ERTX', 'Electronics Engineering')], default='CE', max_length=20),
        ),
    ]
