# Generated by Django 3.2.2 on 2021-05-24 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.EmailValidator(message='Email address is not valid')]),
        ),
    ]
