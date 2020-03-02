# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import ephem
import settings

   
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                                 update.message.chat.id, update.message.text) 
    print(update.message)


"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.


"""
def planet_name(bot, update):
    mars = ephem.Mars()
    mercury = ephem.Mercury()
    venus = ephem.Venus()
    jupiter = ephem.Jupiter()
    saturn = ephem.Saturn()
    uranus = ephem.Uranus()
    neptune = ephem.Neptune()
    pluto = ephem.Pluto() 

    user_text = (update.message.text.split()[1].capitalize().strip())
   
    logging.info(update.message.text)    
    if user_text == "Mars":
        mars.compute()
        update.message.reply_text(ephem.constellation(mars))
    elif user_text == "Mercury":
        mercury.compute()
        update.message.reply_text(ephem.constellation(mercury))
    elif user_text == "Venus":
        venus.compute()
        update.message.reply_text(ephem.constellation(venus))
    elif user_text == "Jupiter":
        jupiter.compute()
        update.message.reply_text(ephem.constellation(jupiter))
    elif user_text == "Saturn":
        saturn.compute()
        update.message.reply_text(ephem.constellation(saturn))
    elif user_text == "Uranus":
        uranus.compute()
        update.message.reply_text(ephem.constellation(uranus))
    elif user_text == "Neptune":
        neptune.compute()
        update.message.reply_text(ephem.constellation(neptune))
    elif user_text == "Pluto":
        pluto.compute()
        update.message.reply_text(ephem.constellation(pluto))
    else:
        update.message.reply_text("Неверное наименование планеты")

    

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
