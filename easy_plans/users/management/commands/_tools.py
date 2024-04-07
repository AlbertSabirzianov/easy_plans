import random
import time

import requests
from art import text2art

from easy_plans import settings
from users.models import School


def upload_schools(url):
    print(random.choice(['...', '..', '.']), sep='\r')
    response = requests.get(
        url,
        headers={'X-API-KEY': settings.API_KEY}
    )
    for data in response.json()['data']:
        new_school = School()
        new_school.name = data['data']['general']['name']
        new_school.description = data['data']['general']['description']
        new_school.address = data['data']['general']['address']['fullAddress']
        new_school.image_url = data['data']['general']['image']['url']
        new_school.save()
    time.sleep(0.2)
    try:
        if response.json()['nextPage']:
            upload_schools(response.json()['nextPage'])
    except KeyError:
        print(text2art('OK'))
