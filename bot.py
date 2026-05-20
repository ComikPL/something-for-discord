import os
import requests

# Pobieranie zmiennych z GitHub Secrets
USER_TOKEN = os.getenv("USER_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

headers = {"Authorization": USER_TOKEN}

def get_last_message():
    # Pobiera ostatnią wiadomość z obserwowanego kanału
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=1"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        messages = response.json()
        return messages[0] if messages else None
    return None

def send_to_webhook(content, author):
    # Wysyła treść na Twój serwer
    data = {
        "username": author,
        "content": content
    }
    requests.post(WEBHOOK_URL, json=data)

if __name__ == "__main__":
    msg = get_last_message()
    if msg:
        # Tutaj musisz dopisać własną logikę sprawdzania, czy wiadomość jest nowa 
        # (np. zapisując ID ostatniej wiadomości do pliku), aby nie wysyłać ciągle tego samego.
        content = msg.get("content")
        author = msg.get("author", {}).get("username", "Ogłoszenie")
        send_to_webhook(content, author)