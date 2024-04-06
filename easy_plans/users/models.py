from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Teacher(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField('email address', unique=True)
    REQUIRED_FIELDS = []


User = get_user_model()


class School(models.Model):

    name = models.TextField(primary_key=True)


class Estimation(models.IntegerChoices):

    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class WorkPlace(models.Model):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Student(models.Model):

    first_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Имя')
    second_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Фамилия')
    sur_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Отчество')
    start_study = models.DateField(null=True, blank=True, verbose_name='Дата поступления в школу')
    end_study = models.DateField(null=True, blank=True, verbose_name='Дата поступления в школу')
    reason = models.TextField(null=True, blank=True, verbose_name='В случае ухода/перехода из школы - причина')
    hearing = models.SmallIntegerField(choices=Estimation.choices, null=True, blank=True, verbose_name='Слух')
    rhythm = models.SmallIntegerField(choices=Estimation.choices, null=True, blank=True, verbose_name='Ритм')
    memory = models.SmallIntegerField(choices=Estimation.choices, null=True, blank=True, verbose_name='Память')
    musical_training = models.SmallIntegerField(
        choices=Estimation.choices,
        null=True,
        blank=True,
        verbose_name='Музыкальная подготовка'
    )
    home_address = models.TextField(null=True, blank=True, verbose_name='Домашний адресс')
    phone = models.CharField(max_length=10, blank=True, null=True, verbose_name='телефон')
    place_of_study = models.TextField(null=True, blank=True, verbose_name='Место учёбы')

    mother = models.CharField(max_length=256, null=True, blank=True, verbose_name='Мать')
    mother_phone = models.CharField(max_length=10, null=True, blank=True, verbose_name='Телефон матери')
    mother_work_place = models.TextField(null=True, blank=True, verbose_name='Место работы/должность матери')

    father = models.CharField(max_length=256, null=True, blank=True, verbose_name='Отец')
    father_phone = models.CharField(max_length=10, null=True, blank=True, verbose_name='Телефон отца')
    father_work_place = models.TextField(null=True, blank=True, verbose_name='Место работы/должность отца')

    work_place = models.ForeignKey(WorkPlace, on_delete=models.CASCADE, related_name='students')
