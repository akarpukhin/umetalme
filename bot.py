from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.chat import Chat
import os
from datetime import datetime
import sys
import time
import configs
import logging


if not os.path.exists(configs.LOG_FILE):
    os.mkdir(os.path.dirname(configs.LOG_FILE))

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=configs.LOG_FILE
                    )


def start(bot, update):

    logging.info('Пользователь {} {} нажал /start'.format(
        update.message.from_user.last_name, update.message.from_user.first_name)
    )

    bot.sendMessage(update.message.chat_id, text="Привет! \n Я - uMetalMeBot! \n\n"
                                                 "Бот, который поможет Вам в поиске концертов\r\n"
                                                 "<b>Основные команды:</b>\n"
                                                 "comming soon\n"
                                                 "<b>debug commands:</b>\n"
                                                 "/exit\n"
                                                 "/reset", parse_mode='HTML')
    return 'Menu'


def stop(bot, update):
    kill_keyboard = ReplyKeyboardRemove()
    bot.sendMessage(
        update.message.chat_id,
        text="До встречи!\r\nМеня можно вызвать командой /start",
        reply_markup=kill_keyboard)
    return ConversationHandler.END


def restart(bot, update):
    bot.send_message(update.message.chat_id, "Bot is restarting...!")
    time.sleep(0.2)
    os.execl(sys.executable, sys.executable, *sys.argv)


main_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        'Menu': [CommandHandler("exit", stop)],
    },

    fallbacks=[CommandHandler("exit", stop)]
)


def main():

    updtr = Updater(configs.TELEGRAM_BOT_KEY)
    updtr.dispatcher.add_handler(main_conversation_handler)

    updtr.dispatcher.add_handler(CommandHandler("reset", restart))
    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started')
    main()
()
