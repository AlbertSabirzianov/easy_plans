# Generated by Django 5.0.2 on 2024-04-13 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_student_hearing_alter_student_memory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=250, null=True, verbose_name='Отделение')),
                ('section', models.CharField(blank=True, max_length=250, null=True, verbose_name='Класс')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='users.student', verbose_name='Студент')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField(verbose_name='год начала')),
                ('end_year', models.IntegerField(verbose_name='год конца')),
                ('result', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Годовая')),
                ('characteristic', models.TextField(verbose_name='Характеристика учащегося на конец учебного года')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='years', to='plans.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='номер четверти')),
                ('repertoire', models.TextField(blank=True, null=True, verbose_name='Репертуар')),
                ('performance', models.TextField(blank=True, null=True, verbose_name='выполнение плана')),
                ('estimation', models.SmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='Оценка')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quarters', to='plans.year')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата экзамена')),
                ('estimation', models.SmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='Оценка')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='plans.year')),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название концерта')),
                ('date', models.DateField(verbose_name='дата концерта')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concerts', to='plans.year')),
            ],
        ),
    ]
