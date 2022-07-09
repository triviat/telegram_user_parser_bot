from telethon import TelegramClient, events
import aiohttp

from time import time

from config import *

client = TelegramClient('user', api_id, api_hash)


async def is_text_in_black_list(text: str) -> bool:
    with open('black_list.txt', encoding='UTF-8') as bl_list:
        black_list = [line.strip().split(', ') for line in bl_list.readlines()]

    for line in black_list:
        is_line_in_message = True

        for word in line:
            if word in text:
                continue
            is_line_in_message = False
            break

        if is_line_in_message:
            return True

    return False


async def is_text_in_white_list(text: str) -> bool:
    with open('white_list.txt', encoding='UTF-8') as wl_list:
        white_list = [line.strip().split(', ') for line in wl_list.readlines()]

    for line in white_list:
        is_line_in_message = True

        for word in line:
            if word in text:
                continue
            is_line_in_message = False
            break

        if is_line_in_message:
            return True

    return False


async def is_message_valid(text: str) -> bool:
    if (not await is_text_in_black_list(text)) and (await is_text_in_white_list(text)):
        return True
    return False


async def save_message(msg: dict) -> None:
    message = {
        "subscriptionName": "UserBotTG",
        "eventType": "new_post",
        "postId": msg['id'],
        "date": int(time()),
        "text": msg['message']
    }

    if msg['peer_id']['_'] == 'PeerChat' or msg['peer_id']['_'] == 'PeerChannel':
        chat = await client.get_entity(msg['peer_id']['channel_id'])
        link = chat.to_dict().get('username', {})
        if link:
            message["link"] = f't.me/{link}/{msg["id"]}'
        else:
            user = await client.get_entity(msg['from_id']['user_id'])
            username = user.to_dict().get('username', {})

            if username:
                message["username"] = f'@{username}'
            else:
                return
    else:
        return

    async with aiohttp.ClientSession() as session:
        await session.post('https://leadbot24.ru/tgstat.php', data=message)


@client.on(events.NewMessage())
async def new_messages_handler(event):
    msg = event.message.to_dict()

    if await is_message_valid(msg['message']):
        await save_message(msg)


if __name__ == '__main__':
    with client:
        client.start()
        client.run_until_disconnected()
