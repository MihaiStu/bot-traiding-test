import os
import requests
from time import sleep

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Mensaje enviado con éxito")
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar mensaje: {e}")

if __name__ == "__main__":
    print("Bot en modo test iniciado...")
    send_telegram_message("✅ Bot de trading activo en modo test.\nTodo listo para operar.")
    while True:
        sleep(3600)  # Mantiene el bot vivo para pruebas (1h por ciclo)
