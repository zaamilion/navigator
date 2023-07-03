from routes import *

from aiogram import types,Bot,Dispatcher,executor

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
msg = None
markup_in = InlineKeyboardMarkup(row_width=3).row(InlineKeyboardButton(text='Спавн', callback_data='m_spawn_'),InlineKeyboardButton(text='exit',callback_data='exit')) 
bot = Bot(token='6213197194:AAGzmFDDnZ-_Py1lgciZQiHfpGOopmNhqGs')
dp = Dispatcher(bot)
def markup_out(callin):
    return  InlineKeyboardMarkup(row_width=3).row(InlineKeyboardButton(text='Спавн', callback_data=callin+'spawn_city_step0'),InlineKeyboardButton(text='Сцена Красногвардейск', callback_data=callin+'krasnogvardeysk_scene_step0'),InlineKeyboardButton(text='exit',callback_data='exit'))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global msg
    msg = await message.answer('КУУУ, откуда едем?',reply_markup=markup_in)

@dp.callback_query_handler()
async def callb(call: types.CallbackQuery):
    global msg
    try:
        await msg.delete()
    except:
        pass
    if call.data == 'exit':
        await call.answer('лады')
        msg = await call.message.answer('КУУУ, откуда едем?',reply_markup=markup_in)
    if call.data[:1]=='m':
        try:
            step = int(call.data[-2]+call.data[-1])
            try:
                i = (globals()[call.data[:-7]])[step+1]
                msg = await call.message.answer_photo((globals()[(call.data[:-7])+'_photo'])[step],reply_markup=InlineKeyboardMarkup(row_width=1).row())
            except:
                pass
            pass
        except:
            try:
                step = int(call.data[-1])
            except:
                await call.message.answer('а куда?',reply_markup=markup_out(call.data))

executor.start_polling(dp)