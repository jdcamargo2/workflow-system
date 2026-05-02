import os
import time
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "http://app:8000")

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN no está definida.")

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id: int, text: str) -> None:
    requests.post(
        f"{TELEGRAM_API}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
        },
        timeout=15,
    )


def create_item(content: str) -> dict:
    response = requests.post(
        f"{API_BASE_URL}/items",
        json={
            "content": content,
            "source": "telegram",
            "status": "pending",
        },
        timeout=15,
    )
    response.raise_for_status()
    return response.json()


def process_update(update: dict) -> None:
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    if not text:
        send_message(chat_id, "Solo puedo procesar texto por ahora.")
        return

    if text == "/start":
        send_message(
            chat_id,
            "Hola, Mango. Envíame una tarea, idea o tema de estudio y lo guardo.",
        )
        return

    if text == "/ping":
        send_message(chat_id, "Sigo vivo 🥭")
        return

    try:
        item = create_item(text)
        send_message(
            chat_id,
            f"Guardado.\nTipo: {item['type']}\nContenido: {item['content']}",
        )
    except Exception as e:
        send_message(chat_id, f"Hubo un error guardando el item: {e}")


def main():
    offset = None

    while True:
        try:
            response = requests.get(
                f"{TELEGRAM_API}/getUpdates",
                params={
                    "timeout": 30,
                    "offset": offset,
                },
                timeout=35,
            )
            response.raise_for_status()
            data = response.json()

            for update in data.get("result", []):
                process_update(update)
                offset = update["update_id"] + 1

        except Exception as e:
            print(f"Error en bot loop: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main()