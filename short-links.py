import argparse
import os
import requests

from dotenv import load_dotenv


URL = 'https://api.vk.com/method/'
METHOD = 'utils.getShortLink'


def shorten_link(token, url):
    headers = {"Authorization": f"Bearer {vk_api_key}", }
    params = {"v": '5.199', 'url': target_url}
    response = requests.get(url=URL+METHOD, headers=headers, params=params)
    response.raise_for_status()
    answer = response.json()
    error = answer.get('error')
    if error:
        raise requests.exceptions.HTTPError(
                URL+METHOD, 400, "Wrong data provided", response=answer
              )
    return answer.get('response').get('short_url')


if __name__ == '__main__':
    load_dotenv(override=True)
    vk_api_key = os.getenv('VK_API_KEY')

    parser = argparse.ArgumentParser(
        description='Укажите ссылку, которую нужно сократить.')
    parser.add_argument('target_url', type=str,
                        help='Target url')
    args = parser.parse_args()
    try:
        target_url = args.target_url
        print(f'Сокращенная ссылка: {shorten_link(vk_api_key, target_url)}')
    except requests.exceptions.HTTPError as exc:
        print(exc)
