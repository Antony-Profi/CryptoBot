from aiogram import types


class CallbackResponse:
    def __init__(self, text: str, replyMarkup: types.InlineKeyboardMarkup):
        self.text = text
        self.replyMarkup = replyMarkup
