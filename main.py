from telethon import TelegramClient, events

# Вводимо API ID та HASH мого тг
api_id = 21340180
api_hash = 'c9f2ebb3b8619dc3ae88991b33f833c8'


# об'єкт Telegram клієнта
client = TelegramClient("TestSession", api_id, api_hash)


target_can =  -1002404770941  # Приклад ID(сюди буде пересилатись повідомлення)

# Ключові слова, які шукати в повідомленнях
key_words = ["Америка", "Американський", "USA", "America"]


# обробляємо події
@client.on(events.NewMessage(chats=[-1002404802004, -1001413275904, -1001405303803,  -1001352726486]))  # Канали в яких йде пошук
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