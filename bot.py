# Импортируем нужные компоненты
from glob import glob
import ephem
import logging
from random import choice
from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters
import settings



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота

def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = 'Привет {}'.format(emo)
    update.message.reply_text(text, reply_markup=get_keyboard())
        
    
    """
    Первая версия приветсвия:
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)
    """



def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Привет, {} {} ! Ты написал: {}".format(update.message.chat.first_name, user_data['emo'],  
                    update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                                 update.message.chat.id, update.message.text) 
    update.message.reply_text(user_text, reply_markup=get_keyboard())


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
def planet_name(bot, update, user_data):
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
        update.message.reply_text(ephem.constellation(mars), reply_markup=get_keyboard())
    elif user_text == "Mercury":
        mercury.compute()
        update.message.reply_text(ephem.constellation(mercury), reply_markup=get_keyboard())
    elif user_text == "Venus":
        venus.compute()
        update.message.reply_text(ephem.constellation(venus), reply_markup=get_keyboard())
    elif user_text == "Jupiter":
        jupiter.compute()
        update.message.reply_text(ephem.constellation(jupiter), reply_markup=get_keyboard())
    elif user_text == "Saturn":
        saturn.compute()
        update.message.reply_text(ephem.constellation(saturn), reply_markup=get_keyboard())
    elif user_text == "Uranus":
        uranus.compute()
        update.message.reply_text(ephem.constellation(uranus), reply_markup=get_keyboard())
    elif user_text == "Neptune":
        neptune.compute()
        update.message.reply_text(ephem.constellation(neptune), reply_markup=get_keyboard())
    elif user_text == "Pluto":
        pluto.compute()
        update.message.reply_text(ephem.constellation(pluto), reply_markup=get_keyboard())
    else:
        update.message.reply_text("Неверное наименование планеты")
#Выдача изображений котов
def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())

#Меняем аватар
def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Готово, Милорд: {}'.format(emo), reply_markup=get_keyboard())

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Готово, Милорд: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Готово, Милорд: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

#генерируем для пользователя эмоджи      
def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']

def get_keyboard():
    contact_button = KeyboardButton('Прислать контакты', request_contact=True)
    location_button = KeyboardButton('Геолокация', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Прислать котэ', 'Сменить аватарку'],
                                        [contact_button, location_button]
                                        ], resize_keyboard=True
                                    )
    return my_keyboard


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("planet", planet_name, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Прислать котэ)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сменить аватарку)$', change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    
    mybot.start_polling()
    mybot.idle()

main()
