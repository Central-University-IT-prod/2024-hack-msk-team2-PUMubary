from aiogram import Bot, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import bot.keyboards as kb
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from collections import defaultdict
from bot.dop import bot
from aiogram.exceptions import TelegramBadRequest
from data.orm import SyncORM

rt = Router()


@rt.message(Command("start"))
async def start(message: Message, state: FSMContext):
    print(message.from_user.username, message.chat.id)
    # print(SyncORM.get_tg_id('dak_dolka'), 'check')
    SyncORM.add_tg_id(message.from_user.username, message.chat.id)
    print(SyncORM.get_tg_id('dak_dolka'), 'inserted')
    await message.answer("Здрасте. Что будем делать?", reply_markup=kb.start_kb)
