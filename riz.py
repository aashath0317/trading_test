import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.sync import events
import telethon

api_id = 3030128
api_hash = 'cfc3885f5d2cbdbc5f10e6a643de2711'
bot_token = '5007713837:AAFAFF-zyIN7XTf_AgM3A-tdKUk6qvfdg60'
channel_ids = [-1001934522827, -1001963686318,-1001518589217, -1001881348526]
GREY = -1001956804894
WFR = -1001855496337
GFR = -1001937116198
# -1518589217 GFR
# -1934522827 GREY
# -1881348526 WFR
string = '1BVtsOLIBu8GjYVUYbXOpCpFA5WwEtrIL8xCiheyWIc2RVqR3cE4ZNYrprDaJl5vvHdYPu-99A7y9pyAD5OeUwVJfdhArO1Tpiy-9fE4LzgFnG_mZBNx0ICfiMryrzOYe7j2SOthcqtpo7_D5IWssEa9o2Ei2npbMDk3OjLE6V_ZUaVRsLNoEM0OI7zwF9FC-0yID7bbHDqUKdWypvQ4MGsrZoUxDzd8r-6wsagfI7dybh22tGy2YDWqpzsgHcR7ZujK0k2nYAxRIazWqLbhWGDDM4I1kxqamyv448BZecB_04RwIRdVPP62d1XF6Or6FMFbmRHnlaQJDRu2JObQdUM5MNGhMs8c='
client = telethon.TelegramClient(StringSession(string), api_id=api_id, api_hash=api_hash)

@client.on(events.NewMessage(chats=channel_ids))
async def send(event):
    from_id = event.message.peer_id.channel_id
    if from_id == 1934522827: #GREY
        await event.message.forward_to(GREY)
    elif from_id == 1518589217: #GFR
        await event.message.forward_to(GFR)
    elif from_id == 1881348526: #WFR
        await event.message.forward_to(WFR)
    elif from_id == 1963686318:
        await event.message.forward_to(GREY)
        await client.send_message(GREY,"TEST")


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
