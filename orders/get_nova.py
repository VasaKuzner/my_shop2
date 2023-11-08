import requests
from django.conf import settings


def get_nova_poshta_data(getSettlementAreas, method_properties):
    api_key = settings.NOVA_POSHTA_API_KEY
    url = 'https://api.novaposhta.ua/v2.0/json/'

    params = {
        'apiKey': api_key,
        'modelName': 'Address',
        'calledMethod': getSettlementAreas,
        'methodProperties': method_properties,
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Handle API request errors here
        return None
