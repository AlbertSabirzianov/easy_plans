from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Teacher(AbstractUser):
    email = models.EmailField('email', unique=True)
    father_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Отчество')

    signature = models.TextField(
        blank=True,
        null=True,
        verbose_name='Подпись'
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'


User = get_user_model()


class School(models.Model):

    name = models.TextField()
    description = models.TextField()
    address = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.name


class Estimation(models.IntegerChoices):

    one = 1, "1"
    two = 2, "2"
    three = 3, "3"
    four = 4, "4"
    five = 5, "5"


class WorkPlace(models.Model):

    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Учебное заведение')
    user = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['school', 'user'],
                name='Уникальная связь Учитель - школа.'
            )
        ]

    def __str__(self):
        return self.school.name


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

    work_place = models.ForeignKey(WorkPlace, on_delete=models.CASCADE, related_name='students', verbose_name='Учебное заведение')
