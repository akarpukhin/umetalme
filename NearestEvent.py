from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


def event(bot, update):
    keyboard = [['Завтра'], ['Послезавтра'], ['Неделя']]
    choice_keyboard = ReplyKeyboardMarkup(keyboard)
    bot.send_message(
        update.message.chat_id,
        text="На какие даты показать ?",
        reply_markup=choice_keyboard)
    return "Menu"
