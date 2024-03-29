import telebot
from weather import Weather

token_file = open('token', 'r')
token = token_file.readline()
bot = telebot.TeleBot(token)

users_cities = {}
w = Weather()
weather_message = (
    'Погода в городе {0}\n'
    'Температура: {1}\n'
    'Небо: {2}\n'
    'Давление: {3} атмосфер\n'
)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Доступные команды:\n/help\n/weather\n/change_city')
    elif message.text == "/weather":
        try:
            w = Weather(users_cities[message.from_user.id])      
            bot.send_message(message.from_user.id,
                            weather_message.format(users_cities[message.from_user.id],
                            w.get_temperature(),
                            w.get_detailed_weather(),
                            w.get_pressure()))
        except KeyError:
            bot.send_message(message.from_user.id, 'Сначала выберите город (/change_city)')
    elif message.text == '/change_city':
        bot.send_message(message.from_user.id, f"Введите свой город: ")
        bot.register_next_step_handler(message, get_city)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def get_city(message):

    check = Weather(message.text).create_user_weather()
    if check == False:
        bot.send_message(message.from_user.id, f'Не найдено место: {message.text}\n'
                                               f'Повторить ввод? /change_city')
        return None

    w = Weather(message.text)
    users_cities[message.from_user.id] = message.text
    bot.send_message(message.from_user.id,
                     weather_message.format(users_cities[message.from_user.id],
                     w.get_temperature(),
                     w.get_detailed_weather(),
                     w.get_pressure()))

        

bot.polling(none_stop=True, interval=0)