from .utils.cons import *
from .utils.utils import load_preset, load_chatgpt_api
from . import config
import asyncio


global chatgpt_api
global L_chatgpt_api
global model


async def bot_start():
    global L_chatgpt_api
    global chatgpt_api
    global model

    cfg = await load_chatgpt_api()
    chatgpt_api = cfg['chatgpt-api']
    L_chatgpt_api = asyncio.Lock()
    model = cfg["model"]

    return cfg


async def Chat(event, foo: Bot, message: str, p: str='', noOut: bool=False):
    if p:
        p = await load_preset(config.presets_dir, config.preset)
        logger.info(f'预设:{p}')
    reply = config.is_reply
    out = await ask(message, p)
    if noOut:
        return out
    await foo.send(event, out, reply_message=reply)


async def ask(message, prompt=''):
    global model
    chatgpt_api.system_prompt = prompt
    chatgpt_api.engine = model
    out = await chatgpt_api.ask_async(message)
    return out
