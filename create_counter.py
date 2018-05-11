from pprint import pprint

import requests


access_token = 'AQAEA7qgxGPDAAT-0JwhPf4-2U3oi0xUjxTmtVc'

response = requests.get('https://api-metrika.yandex.ru/management/v1/counters',
                        headers={'Authorization': 'OAuth {}'.format(access_token)})

pprint(response.json())