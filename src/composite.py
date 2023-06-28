from typing import List

from src.message_handler import Handler


# TODO: consider using asyncio here if performance is an issue
class CompositeListener:
    def __init__(self, message_handlers: List[Handler]):
        self.message_handlers = message_handlers

    def on_message(self, msg):
        for handler in self.message_handlers:
            handler.on_message(msg)

    def on_error(self, msg):
        for handler in self.message_handlers:
            handler.on_error(msg)

    def add_handler(self, handler: Handler):
        self.message_handlers.append(handler)
