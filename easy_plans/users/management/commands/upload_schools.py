from django.core.management import BaseCommand

from ._tools import upload_schools


class Command(BaseCommand):
    help = 'загрузить список музыкальных школ'

    def handle(self, *args, **options):
        upload_schools('https://opendata.mkrf.ru/v2/education/$')
