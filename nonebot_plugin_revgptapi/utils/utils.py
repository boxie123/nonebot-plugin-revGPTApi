import aiofiles
from revChatGPT.V3 import Chatbot as chatGPT_api
from .cons import *
from .. import config

async def load_preset(dir, filename):
    try:
        async with aiofiles.open(dir + "/" + filename, mode="r", encoding='utf-8') as f:
            text = await f.read()
        return text
    except Exception as ERR:
        print(ERR)
        logger.error(f'load_preset 读取预设文件{dir + "/" + filename}失败')
        return
    

async def load_chatgpt_api():
    cfg = {}
    add = ''
    bot = chatGPT_api(api_key=config.api_key)
    models = [
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0301",
        "gpt-4",
        "gpt-4-0314",
        "gpt-4-32k",
        "gpt-4-32k-0314"
    ]
    model = config.model
    if model in models:
        cfg["model"] = model
        add += f',模型: {model}'
    logger.success(f'ChatGPT(api): 已加载{add}')
    cfg['chatgpt-api'] = bot
    return cfg