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
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import BOT_TOKEN

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context) -> None:
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context) -> None:
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planets_chat(update, context) -> None:
    planet_name = update.message.text.split()[1]
    if planet_name == "Mars":
        planet = ephem.Mars(ephem.now())
    elif planet_name == "Mercury":
        planet = ephem.Mercury(ephem.now())
    elif planet_name == "Venus":
        planet = ephem.Venus(ephem.now())
    elif planet_name == "Earth":
        planet = ephem.Earth(ephem.now())
    else:
        update.message.reply_text("Неизвестная планета")

    update.message.reply_text(f"{planet_name} в настоящее время находится в созвездии {ephem.constellation(planet)}.")


def main():
    mybot = Updater(BOT_TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets_chat))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
