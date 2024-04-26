import argparse
import os
import requests

from dotenv import load_dotenv
from urllib.parse import urlparse


URL = 'https://api.vk.com/method/'
SHORTS_LINK = 'utils.getShortLink'
GET_LINK_STATS = 'utils.getLinkStats'


def shorten_link(token, url):
    headers = {"Authorization": f"Bearer {token}", }
    params = {"v": '5.199', 'url': url}
    method_url = URL + SHORTS_LINK
    response = requests.get(url=method_url, headers=headers, params=params)
    response.raise_for_status()
    answer = response.json()
    error = answer.get('error')
    if error:
        raise requests.exceptions.HTTPError(
                method_url, 400, "Wrong data provided", response=answer
              )
    return answer.get('response').get('short_url')


def count_clicks(token, url):
    link = urlparse(url).path[1:]
    headers = {"Authorization": f"Bearer {token}", }
    params = {"v": '5.199', 'key': link}
    method_url = URL + GET_LINK_STATS
    response = requests.get(url=method_url, headers=headers,
                            params=params)
    response.raise_for_status()
    answer = response.json()
    error = answer.get('error')
    if error:
        raise requests.exceptions.HTTPError(
                method_url, 400, "Wrong data provided", response=error
              )
    stats = answer.get('response').get('stats')
    return stats[0].get('views') if stats else 0


def is_shorten_link(url):
    return urlparse(url).netloc == 'vk.cc'


if __name__ == '__main__':
    load_dotenv(override=True)
    vk_api_key = os.getenv('VK_API_KEY')

    parser = argparse.ArgumentParser(
        description='Укажите ссылку.')
    parser.add_argument('target_url', type=str,
                        help='Enter url')
    args = parser.parse_args()
    try:
        target_url = args.target_url
        if is_shorten_link(target_url):
            print('Число переходов по ссылке: '
                  f'{count_clicks(vk_api_key, target_url)}')
        else:
            print('Сокращенная ссылка: '
                  f'{shorten_link(vk_api_key, target_url)}')
    except requests.exceptions.HTTPError as exc:
        print(f'{exc=}')
