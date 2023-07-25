from aiogram import Bot, Dispatcher, executor, types
import telebot

API_TOKEN = '6681267904:AAFCri40fBiXgtRYej5ZiwdV0FvMyIH4yRc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ помощник для тебя по Питону\nОтправь сообщение /help, чтобы увидеть, что я могу")


@dp.message_handler(commands=['forAnderey'])
async def Anrei(message: types.Message):
    await message.reply("Я тебя люблю")


@dp.message_handler(commands=['help'])  # Доступные команды
async def help(message: types.Message):
    await message.reply("Документ по словарям /dict\n"
                        "Документ по библиотекам /lib\n"
                        "Удалить все сообщения /del")


@dp.message_handler(commands=['dict'])  # Вызываем фотку с словарями
async def dictionary(message: types.Message):
    doc = open("/home/jeimaster/Рабочий стол/py/TelegramBot/venv/py04.pdf", "rb")
    await message.reply_document(doc)

@dp.message_handler(commands=['lib'])  # Вызываем фотку с Библами
async  def lib(message: types.Message):
    doc = open("/home/jeimaster/Рабочий стол/py/TelegramBot/venv/py06.pdf", "rb")
    await message.reply_document(doc)



#@dp.message_handler(commands=['del'])  # Вызываем фотку с Библами
    #async  def delet(message: types.Message):


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
