from telethon import TelegramClient, events, sync
import aiohttp
from bs4 import BeautifulSoup
import os


# Remember to use your own values from my.telegram.org!
api_id = int(os.environ['api_id'])
api_hash = os.environ['api_hash']
client = TelegramClient('mxdownload', api_id, api_hash)

# @client.on(events.NewMessage(chats='khazinml'))
# async def my_event_handler(event):
#     print(event.raw_text)

# client.start()
# client.run_until_disconnected()

async def getLinkContent(uri):
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:
            html = await response.text()
    return html

def getKaleidoscopeLink(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.iframe['src']

async def main():
    cnt = 0
    # You can print the message history of any chat:
    async for message in client.iter_messages('khazinml'):
        cnt += 1
        if cnt > 100:
            break
        # print(message.id, message.text, message)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.photo and 'https://khazin.ru/' in message.text:
            print(message.date, message.text)  # printed after download is done

with client:
    client.loop.run_until_complete(main())
