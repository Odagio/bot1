from glob import glob
from random import choice
from utils import get_smile, main_keyboard, play_random_numbers

def greet_user(update, context):
     context.user_data['emoji'] = get_smile(context.user_data)
     print('вызван/start')
     update.message.reply_text(
          f"Здравствуй, пользователь {context.user_data['emoji']}!",
          reply_markup=main_keyboard()
          ) 


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
     update.message.reply_text(message, reply_markup=main_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text 
    print(user_text)
    print(update)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}")


def user_coordinates (update, context):
     context.user_data['emoji'] = get_smile(context.user_data)
     coords = update.message.location
     update.message.reply_text(
          f"Ваши координаты {coords} {context.user_data['emoji']}!"
     )

def send_cat_picture (update, context):
     cat_photo_list = glob('images/cat*.jp*g')
     cat_photo_filename =choice(cat_photo_list)
     chat_id = update.effective_chat.id
     context.bot.send_photo( chat_id=chat_id, photo = open(cat_photo_filename,'rb'), 
     reply_markup=main_keyboard())
