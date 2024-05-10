from django.contrib.auth import get_user_model
from django.test import TestCase

from documents.document_creater import DocumentMaker
from plans.models import Plan
from users.models import School, WorkPlace, Student

User = get_user_model()


class DocumentTestCase(TestCase):

    user = None
    work_place = None
    school = None
    student = None
    plan = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='test',
            email='test@mail.com',
            password='test'
        )

        cls.school = School()
        cls.school.name = 'Лучшая школа'
        cls.school.address = 'test'
        cls.school.description = 'test'
        cls.school.save()

        cls.work_place = WorkPlace(
            user=cls.user,
            school=cls.school
        )
        cls.work_place.save()

        cls.student = Student()
        cls.student.first_name = 'Саша'
        cls.student.second_name = 'Малинович'
        cls.student.work_place = cls.work_place
        cls.student.save()

        cls.plan = Plan()
        cls.plan.student = cls.student
        cls.plan.department = 'test'
        cls.plan.section = 'test'
        cls.plan.save()

    # def test_title(self):
    #     dx = DocumentMaker(Plan.objects.first())
    #     doc = dx.get_document()
    #     doc.save('dx.docx')

