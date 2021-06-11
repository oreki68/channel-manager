import time
from config import client as client
from telethon import events

@client.on(events.NewMessage(pattern=("\+help")))
async def help_function(event):
    await event.edit("Commands avilabe:-\n\n`+ping` - Just a confirmation that bot is working\n\n`+fwd :<username of channel>:<start_id>:<end_id>` - Forward a bunch of files without forwarded from tag\n\n`+edit :<username of group where corrected file is located>:<correct file message_id>` if you messed up sequence in channel (reply this command to the file you want to edit)\n\n\n*Note if channel/group you are working with is private in place of username put invite link starting from `joinchat/.....`")

@client.on(events.NewMessage(pattern=("\+ping")))
async def hi_function(event):
    await event.edit("pong")

@client.on(events.NewMessage(pattern=("\+fwd")))
async def fwd_function(event):
    try:
        await event.edit("okay, on it")
        split = event.raw_text.split(":")
        username_of_channel = split[1]
        start_id = int(split[2])
        end_id = int(split[3])+1
        channel = await client.get_entity(f"t.me/{username_of_channel}")
        for i in range(start_id, end_id):
            print("hi")
            try:
                message = await client.get_messages(channel, ids=i)
                await client.send_message(event.chat_id, message)
            except:
                pass
            time.sleep(0.25)
    except:
        pass

    await client.send_message(event.chat_id, "done")

@client.on(events.NewMessage(pattern=("\+edit")))
async def edit_function(event):
    split = event.raw_text.split(":")
    username = split[1]
    msg_id = int(split[2])
    reply = await event.get_reply_message()
    entity = await client.get_entity(f"t.me/{username}")
    message = await client.get_messages(entity, ids=msg_id)
    await event.edit("Editing the message holup....")
    await client.edit_message(reply, file=message.media, force_document=True)
    await event.edit("Done")

@client.on(events.NewMessage(pattern=("\+purge")))
async def purge(event):
    split = event.raw_text.split(":")
    start = int(split[1])
    end = int(split[2]) + 1
    for i in range(start, end):
        try:
            message = await client.get_messages(event.chat_id, ids=i)
            await message.delete()
        except:
            pass
        time.sleep(0.25)

client.start()

client.run_until_disconnected()
