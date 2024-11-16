from aiogram import Bot
from bot.config import settings
print(settings.TOKEN)
bot = Bot(settings.TOKEN)