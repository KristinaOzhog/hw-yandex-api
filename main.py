import requests
from pprint import pprint


TOKEN = ''


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path, filename):
        link_dict = self._get_upload_link(file_path=file_path)
        href = link_dict.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    pprint(ya.upload('netology/test_to_upload.txt', 'test_to_upload.txt'))

