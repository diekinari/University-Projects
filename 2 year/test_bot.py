import asyncio
import logging
from aiogram import Bot, Dispatcher, types, enums
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

from gptScript import normalize_chatgpt_notation  # Импорт функции обработки текста

# Получаем токен бота из переменных окружения или замените на свой токен
API_TOKEN = ""

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()


# Определяем класс состояний для команды /convert
class ConvertState(StatesGroup):
    waiting_for_text = State()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Отправь команду /convert и текст, который нужно преобразовать в Markdown.\nНапример:\n/convert Твой текст здесь")


@dp.message(Command("convert"))
async def cmd_convert(message: types.Message, state: FSMContext):
    await message.reply("Пожалуйста, отправьте текст для преобразования:")
    await state.set_state(ConvertState.waiting_for_text)


@dp.message(ConvertState.waiting_for_text)
async def process_conversion(message: types.Message, state: FSMContext):
    text = message.text
    converted_text = normalize_chatgpt_notation(text)
    await message.reply(converted_text)
    await state.clear()

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
