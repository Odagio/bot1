
from emoji import emojize
from glob import glob
import logging
from random import choice, randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
     context.user_data['emoji'] = get_smile(context.user_data)
     print('вызван/start')
     update.message.reply_text(f'Привет, пользователь{context.user_data}!') 

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text 
    print(user_text)
    print(update)
    update.message.reply_text(f'{user_text} {context.user_data}')

def get_smile(user_data):
     if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases = True)
     return user_data['emoji']


def play_random_numbers(user_number):
     bot_number = randint(user_number -10, user_number + 10)
     if user_number > bot_number:
          message = f'ваше число {user_number} , мое {bot_number}, вы выиграли'
     elif user_number == bot_number:
          message = f'ваше число {user_number} , мое {bot_number}, ничья'
     else:
          message = f'ваше число {user_number} , мое {bot_number}, вы проиграли'
     return message


def guess_number(update, context):
     print(context.args)
     if context.args:
          try:
               user_number = int(context.args[0])
               message = play_random_numbers (user_number)
          except (TypeError,ValueError):
               message = "введите целое число"
               
     else:
          message = "Введи число"
     update.message.reply_text(message)
def send_cat_picture (update, context):
     cat_photo_list = glob('images/cat*.jp*g')
     cat_photo_filename =choice(cat_photo_list)
     chat_id = update.effective_chat.id
     context.bot.send_photo( chat_id=chat_id, photo = open(cat_photo_filename,'rb'))

def main():
     mybot = Updater(settings.API_KEY, use_context=True)
     dp = mybot.dispatcher
     dp.add_handler(CommandHandler ("start", greet_user))
     dp.add_handler(CommandHandler ("guess", guess_number))
     dp.add_handler(CommandHandler ("cat", send_cat_picture))
     dp.add_handler(MessageHandler(Filters.text, talk_to_me))
     logging.info("Бот стартовал")
     mybot.start_polling()
     mybot.idle()

if __name__ == "__main__":
     main()