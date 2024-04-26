# Создание коротких ссылок с помощью [API VK](https://dev.vk.com/ru/method/utils)

## Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```sh
pip install -r requirements.txt
```

## Подготовка

В личном кабинете VK [создайте приложение](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application) и получите для него [сервисный токен](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/tokens/service-token)
Создайте файл с настройками `.env` и положите в него полученный токен:

## Использование

Чтобы сократить ссылку:

```sh
python short-links.py <ссылка которую нужно сократить>
```

Чтобы получить статистику по ссылке:

```sh
python short-links.py <короткая ссылка>
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
