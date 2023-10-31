import requests


def send_telegram_message(chat_id, message, token):
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    data = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, json=data)
    return response.json()

