from nonebot import get_driver
from dotenv import load_dotenv

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)
load_dotenv()

from . import msg_handle
