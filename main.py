from telethon import TelegramClient, events

# Вводимо API ID та HASH мого тг
api_id = 1234567
api_hash = 'abcdef123456abcdef123456abcdef12'


# об'єкт Telegram клієнта
client = TelegramClient("TestSession", api_id, api_hash)


target_can = -1009876543210  # Приклад ID(сюди буде пересилатись повідомлення)

# Ключові слова, які шукати в повідомленнях
key_words = ["Америка", "Американський", "USA", "America"]


# обробляємо події
@client.on(events.NewMessage(chats=[-1001234567890, -1009876543210]))  # Канали в яких йде пошук
async def normal_handler(event):
    # Перебираємо ключі
    for word in key_words:
        # Наявність ключових слів
        if word in event.message.message:
            print(f"Знайдено повідомлення: {event.message.message}")
            print(f"ID чату/групи: {event.message.peer_id}")

            # Пересилаємо знайдене повідомлення в мій канал
            await client.send_message(target_can, event.message)
            break



client.start()
client.run_until_disconnected()  # цикл поки не вимкну