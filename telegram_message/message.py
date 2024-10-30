import requests


class TelegramBotError(Exception):
    """Custom exception for Telegram bot errors."""
    def __init__(self, message):
        super().__init__(message)


class TelegramMessage:
    """
    A class to send messages via a Telegram bot.

    Attributes:
        bot_token (str): The Telegram bot token.
        chat_id (str, optional): Default chat ID for messages.
        parse_mode (str, optional): Formatting option for messages ('markdown' or 'HTML').
        disable_web_page_preview (bool, optional): Disable link previews in messages.
        timeout (int, optional): Request timeout in seconds.
        proxies (dict, optional): Proxy settings for requests.

    Methods:
        send: Send text messages.

    Proxies attribute example:
    - With login and password:
    {'proxies': {'http': 'socks5://user:login@1.2.3.4:1234', 'https': 'user:login@1.2.3.4:1234'}}
    - Without login and password:
    {'proxies': {'http': 'socks5://1.2.3.4:1234', 'https': '1.2.3.4:1234'}}
    """

    def __init__(self, bot_token, chat_id=None,
                 parse_mode='markdown', disable_web_page_preview=False, timeout=10, proxies=None):
        self._bot_token = bot_token
        self._chat_id = chat_id
        self._parse_mode = parse_mode
        self._disable_web_page_preview = disable_web_page_preview
        self._timeout = timeout
        self._proxies = proxies if proxies else ''

    def _send_request(self, method, payload):
        """Internal method to send requests to the Telegram API."""
        api_url = f"https://api.telegram.org/bot{self._bot_token}/{method}"
        try:
            response = requests.post(api_url, data=payload, timeout=self._timeout, proxies=self._proxies)
            response.raise_for_status()  # Raises stored HTTPError, if one occurred.
            return response.json()  # Returns the response in JSON format.
        except requests.exceptions.RequestException as e:
            raise TelegramBotError(f"Request to Telegram API failed: {e}")

    def send(self, message, chat_id=None):
        """
        Send a text message to a specified chat via Telegram bot.

        Parameters:
            message (str): The message text to send.
            chat_id (str, optional): The chat ID. Overrides the default if provided.

        Returns:
            dict: The response from Telegram API.

        Raises:
            TelegramBotError: If chat ID is not specified or an API request fails.
        """
        if not chat_id and not self._chat_id:
            raise TelegramBotError('Chat ID unknown')

        chat_id = chat_id or self._chat_id  # Use provided chat_id or default to self.chat_id
        params = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': self._parse_mode,
            'disable_web_page_preview': str(self._disable_web_page_preview).lower()
        }

        return self._send_request('sendMessage', params)


# Example Usage
if __name__ == "__main__":
    bot = TelegramMessage('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')
    try:
        # Sending a text message
        response = bot.send('Hello, world!')
        print(response)
    except TelegramBotError as e:
        print(e)
