from urllib.parse import urlencode

app_id = '947e453e39b74638a4ec6b0c52b646c7'
auth_url = 'https://oauth.yandex.ru/authorize?'
auth_param = {
    'response_type': 'token',
    'client_id': app_id,
}
print('&'.join((auth_url, urlencode(auth_param))))

access_token = 'AQAEA7qgxGPDAAT-0JwhPf4-2U3oi0xUjxTmtVc'