from weather import get_weather, get_forecast
import telebot
from telebot import types


bot = telebot.TeleBot("YOUR_TOKEN")


@bot.message_handler(commands=['start'])
def meeting_message(message):
    bot.send_message(message.chat.id, text="""
                    Hello, """ + message.chat.first_name)

    bot.send_message(message.chat.id, text="""
to see weather just write your city after command:
`weather`(to find out the weather in this city) or
`forecast`(to get forecast for your city)""")


#weather for now
@bot.message_handler(commands=['weather'])
def weather(message):
    misto = message.text.split('/weather ')[1]

    try:
        weather = get_weather(misto)
    except:
        bot.send_message(message.chat.id,
                    text=f"""Can you enter the command more correctly,
I don't know anything about {misto}""")

    bot.send_message(message.chat.id, text=f"{weather[0]}\n{weather[1]}\n{weather[2]}")


#forecasts for different times
@bot.message_handler(commands=['forecast'])
def forecast(message):
    misto = message.text.split('/forecast ')[1]

    i = 1

    try:
        forecast = get_forecast(misto, i)
    except:
        bot.send_message(message.chat.id,
                    text=f"""Can you enter the command more correctly,
I don't know anything about {misto}""")


    markup = types.InlineKeyboardMarkup() #markup that lets you switch forecasts
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton(text="<", callback_data=f"previous2{misto}.{i}"),
        types.InlineKeyboardButton(text=">", callback_data=f"next1{misto}.{i}"))

    bot.send_message(message.chat.id,
                        text=f"{forecast[0]}\n{forecast[1]}\n{forecast[2]}\n{forecast[3]}",
                        reply_markup=markup)


#code that switches forecasts to different times, it lisens calls like from line 48/49
@bot.callback_query_handler(func=lambda call: True)
def answer(call):

    if call.data.startswith("next1"):
        misto = call.data.split('next1')[1].split('.')[0]

        i = int(call.data.split('.')[1]) + 1

        print(i)

        try:
            forecast = get_forecast(misto, i)

            markup = types.InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(types.InlineKeyboardButton(text="<", callback_data=f"previous2{misto}.{i}"),
            types.InlineKeyboardButton(text=">", callback_data=f"next1{misto}.{i}"))
            
            bot.edit_message_text(text=f"{forecast[0]}\n{forecast[1]}\n{forecast[2]}\n{forecast[3]}",
                                chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
        except:...


    elif call.data.startswith("previous2"):
        misto = call.data.split('previous2')[1].split('.')[0]

        i = int(call.data.split('.')[1]) - 1

        print(i)

        try:
            forecast = get_forecast(misto, i)
        
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(types.InlineKeyboardButton(text="<", callback_data=f"previous2{misto}.{i}"),
            types.InlineKeyboardButton(text=">", callback_data=f"next1{misto}.{i}"))

            bot.edit_message_text(text=f"{forecast[0]}\n{forecast[1]}\n{forecast[2]}\n{forecast[3]}",
                                chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
        except:...


bot.infinity_polling()
