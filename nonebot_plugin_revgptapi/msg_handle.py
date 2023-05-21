import asyncio
from nonebot import on_command

from .utils.cons import *

from .bot import Chat, bot_start

cfg = asyncio.run(bot_start())

chat = on_command("chat", priority=1, block=True)
preset_chat = on_command("preset", priority=1, block=True)

@chat.handle()
async def _(foo: Bot, event: GroupMessageEvent | PrivateMessageEvent, args: Message = CommandArg()):
    message = args.extract_plain_text()
    if len(message) == 0: return
    logger.info(f'对话: {message}')
    await Chat(event, foo, message)


@preset_chat.handle()
async def _(foo: Bot, event: GroupMessageEvent | PrivateMessageEvent, args: Message = CommandArg()):
    message = args.extract_plain_text()
    if len(message) == 0: return
    logger.info(f'预设对话: {message}')
    await Chat(event, foo, message, p='preset')