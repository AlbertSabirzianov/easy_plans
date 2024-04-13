from django.db import models

from users.models import Student, Estimation


class Plan(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='plans',
        verbose_name='Студент'
    )
    department = models.CharField(
        max_length=250,
        verbose_name='Отделение',
        null=True,
        blank=True
    )
    section = models.CharField(
        max_length=250,
        verbose_name='Класс',
        null=True,
        blank=True
    )


class Year(models.Model):

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name='years'
    )
    start_year = models.IntegerField(
        verbose_name='год начала'
    )
    end_year = models.IntegerField(
        verbose_name='год конца'
    )
    result = models.SmallIntegerField(
        choices=Estimation.choices,
        verbose_name='Годовая'
    )
    characteristic = models.TextField(
        verbose_name='Характеристика учащегося на конец учебного года'
    )


class Quarter(models.Model):
    year = models.ForeignKey(
        Year,
        on_delete=models.CASCADE,
        related_name='quarters'
    )
    number = models.SmallIntegerField(
        verbose_name='номер четверти'
    )
    repertoire = models.TextField(
        verbose_name='Репертуар',
        blank=True,
        null=True
    )
    performance = models.TextField(
        verbose_name='выполнение плана',
        blank=True,
        null=True
    )
    estimation = models.SmallIntegerField(
        choices=Estimation.choices,
        verbose_name='Оценка',
        blank=True,
        null=True
    )


class Concert(models.Model):

    year = models.ForeignKey(
        Year,
        on_delete=models.CASCADE,
        related_name='concerts'
    )
    name = models.CharField(
        max_length=250,
        verbose_name='Название концерта'
    )
    date = models.DateField(
        verbose_name='дата концерта'
    )


class Exam(models.Model):

    year = models.ForeignKey(
        Year,
        related_name='exams',
        on_delete=models.CASCADE
    )
    date = models.DateField(
        verbose_name='дата экзамена'
    )
    estimation = models.SmallIntegerField(
        choices=Estimation.choices,
        verbose_name='Оценка',
        blank=True,
        null=True
    )



