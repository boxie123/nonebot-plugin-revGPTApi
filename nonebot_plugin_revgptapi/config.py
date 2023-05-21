from pydantic import BaseSettings, Extra, validator
from pydantic.fields import ModelField

class Config(BaseSettings):
    """Plugin Config Here"""
    fastapi_reload: bool = False
    api_url: str = "https://api.chatanywhere.com.cn/v1/chat/completions"
    api_key: str = ""
    model: str = "gpt-4"
    preset: str = "PromptGenerator.txt"
    stream_wait_time: int = 2
    is_reply: bool = True
    is_stream: bool = False
    presets_dir: str = "./presets"

    class Config:
        extra = Extra.ignore

    @validator("api_key")
    def check_api_key(cls, v: str):
        if v.startswith("sk-"):
            return v
        else:
            raise ValueError("api_key不合法")
        
    @validator("stream_wait_time")
    def check_wait_time(cls, v: int, field: ModelField):
        if v < 1:
            return field.default
        return v
