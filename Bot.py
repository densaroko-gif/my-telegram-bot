import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Твой токен вставлен
TOKEN = '8963839939:AAGoySnPfdNP__HdAFSpaUm8VR6zv6UjTeo'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("mute"))
async def mute_command(message: Message):
    if message.reply_to_message:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except Exception:
            await message.answer("Ошибка: дай мне права администратора!")
    else:
        await message.answer("Ответь на сообщение, которое нужно удалить.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
