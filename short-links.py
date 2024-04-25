import os
import requests

from dotenv import load_dotenv


URL = 'https://api.vk.com/method/'
METHOD = 'utils.getShortLink'


if __name__ == '__main__':
    load_dotenv(override=True)
    vk_api_key = os.getenv('VK_API_KEY')

    target_url = 'https://dvmn.org/modules'
    headers = {"Authorization": f"Bearer {vk_api_key}", }
    params = {"v": '5.199', 'url': target_url}
    response = requests.get(url=URL+METHOD, headers=headers, params=params)
    response.raise_for_status()
    print(f'{response.json()=}')
