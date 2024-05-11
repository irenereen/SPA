# Generated by Django 5.0.6 on 2024-05-10 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('therapist', 'Therapist'), ('receptionist', 'Receptionist'), ('hairdreser', 'Hairdreser')], max_length=20)),
                ('shift_start_time', models.TimeField()),
                ('shift_end_time', models.TimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]