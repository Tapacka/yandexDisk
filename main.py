import requests

token = ''


def get_headers():
    return {'Content-type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}


def get_upload_link(disk_file_path):
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    headers = get_headers()
    params = {'path': disk_file_path, 'overwrite': 'true'}
    response = requests.get(upload_url, headers=headers, params=params)
    return response.json()


def upload_file_to_disk(disk_file_path):
    href = get_upload_link(disk_file_path=disk_file_path).get('href', '')
    response = requests.put(href, data=open(disk_file_path, 'rb'))
    response.raise_for_status()
    if response.status_code == 201:
        print('success')


upload_file_to_disk('test.txt')