<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-revGPTApi

_✨ 通过GPTApi在QQ上与ChatGPT对话，支持GPT4 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-example.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-example">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-example.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

找了一圈没找到能用api、能简单设置反代、而且支持GPT-4的插件，只好自己写一个

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-revgptapi

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-revgptapi
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-revgptapi
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-revgptapi
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-revgptapi
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_revgptapi"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| API_KEY | 是 | 无 | api key |
| API_URL | 否 | https://api.chatanywhere.com.cn/v1/chat/completions | 默认使用[GPT_API_free](https://github.com/chatanywhere/GPT_API_free)仓库的反代链接 |
| MODEL | 否 | gpt-4 | 使用的模型 |
| PRESET | 否 | PromptGenerator.txt | 预设模板文件名 |

其余配置请自行查看`config.py`

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| chat | 无 | 是 | 私聊和群聊 | 聊天 |
| preset | 无 | 是 | 私聊和群聊 | 启用预设模板并聊天 |

## 鸣谢
- [GPT_API_free](https://github.com/chatanywhere/GPT_API_free): 提供稳定的反代链接和廉价api额度
- [SDGPT](https://github.com/thx114/SDGPT): 提供插件实现思路
- [revChatGPT](https://github.com/acheong08/ChatGPT): 提供功能实现工具