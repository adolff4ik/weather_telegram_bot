from weather import get_weather, get_forecast
import telebot


bot = telebot.TeleBot("YOUR_TOKEN")


@bot.message_handler(commands=['start'])
def meeting_message(message):
    bot.send_message(message.chat.id, text="""
                    Hello, """ + message.chat.first_name)

    bot.send_message(message.chat.id, text="""
to see weather just write your city after command:
`weather`(to find out the weather in this city) or
`forecast`(to get forecast for your city)""")

@bot.message_handler(commands=['weather'])
def weather(message):
    misto = message.text.split('/weather ')[1]

    weather = get_weather(misto)

    bot.send_message(message.chat.id, text=f"""{weather[0]}\n{weather[1]}\n{weather[2]}""")

@bot.message_handler(commands=['forecast'])
def forecast(message):
    misto = message.text.split('/forecast ')[1]

    for i in range(40):
        forecast = get_forecast(misto, i)
        bot.send_message(message.chat.id,
                            text=f"""{forecast[0]}\n{forecast[1]}\n{forecast[2]}\n{forecast[3]}""")


bot.infinity_polling()