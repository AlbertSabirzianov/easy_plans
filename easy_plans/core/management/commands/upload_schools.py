from django.core.management import BaseCommand

from ._tools import upload_schools, is_school_table_empty


class Command(BaseCommand):
    help = 'загрузить список музыкальных школ'

    def handle(self, *args, **options):
        if is_school_table_empty():
            upload_schools('https://opendata.mkrf.ru/v2/education/$')
        else:
            print()