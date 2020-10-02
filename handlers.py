from glob import glob
import os
from random import choice

from db import db, get_or_create_user
from utils import  is_cat, main_keyboard, play_random_numbers

def greet_user(update, context):
     print('вызван/start')
     user = get_or_create_user(db, update.effective_user,update.message.chat.id)
     update.message.reply_text(
          f"Здравствуй, пользователь {user['emoji']}!",
          reply_markup=main_keyboard()
          ) 


def guess_number(update, context):
     user = get_or_create_user(db, update.effective_user,update.message.chat.id)
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
     user = get_or_create_user(db, update.effective_user,update.message.chat.id)
     
     user_text = update.message.text 
     print(user_text)
     print(update)
     update.message.reply_text(f"{user_text} {user['emoji']}")


def user_coordinates (update, context):
     user = get_or_create_user(db, update.effective_user,update.message.chat.id)
     coords = update.message.location
     update.message.reply_text(
          f"Ваши координаты {coords} {user['emoji']}!"
     )

def send_cat_picture (update, context):
     user = get_or_create_user(db, update.effective_user,update.message.chat.id)
     cat_photo_list = glob('images/cat*.jp*g')
     cat_photo_filename =choice(cat_photo_list)
     chat_id = update.effective_chat.id
     context.bot.send_photo( chat_id=chat_id, photo = open(cat_photo_filename,'rb'), 
     reply_markup=main_keyboard()
     )

def check_user_photo (update, context):
     user = get_or_create_user(db, update.effective_user,update.message.chat.id)
     update.message.reply_text("обрабатываю фото")
     os.makedirs("downloads", exist_ok=True)
     user_photo = context.bot.getFile(update.message.photo[-1].file_id)
     file_name = os.path.join ("downloads",f"{user_photo.file_id}.jpg")
     user_photo.download(file_name)
     if is_cat(file_name):
        update.message.reply_text("Обнаружен котавый))")
        new_filename = os.path.join("images",f"cat_{user_photo.file_id}.jpg")
        os.rename(file_name, new_filename)
     else:
        update.message.reply_text("Это не кот!")
        os.remove(file_name)

    
    