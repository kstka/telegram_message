# TelegramMessage
TelegramMessage is a simple Python package for sending messages through a Telegram bot.

# Features
* Send text messages via Telegram bot.
* Support for markdown or HTML message formatting.
* Option to disable web page previews in messages.
* Proxy support

# Installation
```
git clone https://github.com/kstka/telegram_message
cd telegram_message
pip install .
```

# Usage
```python
from telegram_message import TelegramMessage

bot = TelegramMessage('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')

response = bot.send('Hello, world!')
print(response)

response = bot.send('Hi there!', 'YOUR_OTHER_CHAT_ID')
print(response)
```

With proxy:
```python
from telegram_message import TelegramMessage

proxy = 'socks5://user:login@1.2.3.4:1234'
proxies = {'proxies': {'http': proxy, 'https': proxy}}

bot = TelegramMessage('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID', proxies=proxies)
```

# License
MIT

