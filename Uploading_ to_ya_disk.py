from pprint import pprint
import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "true"}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        response = requests.get(upload_url, headers=headers, params=params)
        json_resp = response.json()
        href = json_resp.get('href', '')
        resp = requests.put(url=href, data=open(filename, 'rb'))
        resp.raise_for_status()
        print("Файл загружен!")



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input("Введите, куда помесить файл\n")
    filename = input("Введите название файла с расширением\n")
    token = input("Введите токен\n")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, filename)