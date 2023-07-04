from routes import *

from aiogram import types,Bot,Dispatcher,executor

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from gtts import gTTS

msgp = None
msg = None
markup_in = InlineKeyboardMarkup(row_width=3).row(InlineKeyboardButton(text='Спавн', callback_data='m_spawn_'),InlineKeyboardButton(text='exit',callback_data='exit')) 
bot = Bot(token='6213197194:AAGzmFDDnZ-_Py1lgciZQiHfpGOopmNhqGs')
dp = Dispatcher(bot)
def markup_out(callin):
    return  InlineKeyboardMarkup(row_width=3).row(InlineKeyboardButton(text='Спавн', callback_data=callin+'spawn_city_pre'),InlineKeyboardButton(text='Сцена Красногвардейск', callback_data=callin+'krasnogvardeysk_scene_pre'),InlineKeyboardButton(text='exit',callback_data='exit'))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global msg
    msg = await message.answer('КУУУ, откуда едем?',reply_markup=markup_in)

@dp.callback_query_handler()
async def callb(call: types.CallbackQuery):
    global msg, msgp
    try:
        await msgp.delete()
    except:
        pass
    try:
        await msg.delete()
    except:
        pass
    if call.data == 'exit':
        await call.answer('restarted')
        msg = await call.message.answer('КУУУ, откуда едем?',reply_markup=markup_in)
    elif call.data[:1]=='m':
        print(1)
        try:
            step = int(call.data[-2]+call.data[-1])
            print(2)
            try:
                i = (globals()[call.data[:-7]])[step+1]
                msgp = await call.message.answer_photo((globals()[(call.data[:-7])+'_photo'])[step],reply_markup=InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Едем дальше',callback_data=call.data[:-2]+str(step+1))))
            except:
                msgp = await call.message.answer_photo((globals()[(call.data[:-7])+'_photo'])[step],reply_markup=InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Закончить поездку',callback_data=call.data[:-2]+'end')))
        except:
            try:
                step = int(call.data[-1])
                try:
                    i = (globals()[call.data[:-6]])[step+1]
                    msgp = await call.message.answer_photo((globals()[(call.data[:-6])+'_photo'])[step],reply_markup=InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Едем дальше',callback_data=call.data[:-1]+str(step+1))))
                except:
                    print(3)
                    msgp = await call.message.answer_photo((globals()[(call.data[:-6])+'_photo'])[step],reply_markup=InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Закончить поездку',callback_data=call.data[:-2]+'end')))
            except:
                print(call.data[-3:])
                if call.data[-3:]=='end':
                    msg = await call.message.answer('поездка успешно завершена',reply_markup=InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Начать новую поездку',callback_data='exit')))
                elif call.data[-3:]=='pre':
                    msgp = await call.message.answer_photo((globals()[call.data]),caption='Маршрут построен',reply_markup=InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Поехали',callback_data=call.data[:-3]+'step0'),InlineKeyboardButton(text='exit',callback_data='exit')))
                else:
                    msg = await call.message.answer('а куда?',reply_markup=markup_out(call.data))

executor.start_polling(dp)