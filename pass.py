
# def greet_user(update, context):
#      context.user_data['emoji'] = get_smile(context.user_data)
#      print('вызван/start')
#      update.message.reply_text(
#           f"Здравствуй, пользователь {context.user_data['emoji']}!",
#           reply_markup=main_keyboard()
#           ) 

# def talk_to_me(update, context):
#     context.user_data['emoji'] = get_smile(context.user_data)
#     user_text = update.message.text 
#     print(user_text)
#     print(update)
#     update.message.reply_text(f"{user_text} {context.user_data['emoji']}")

# def get_smile(user_data):
#      if 'emoji' not in user_data:
#         smile = choice(settings.USER_EMOJI)
#         return emojize(smile, use_aliases = True)
#      return user_data['emoji']


# def play_random_numbers(user_number):
#      bot_number = randint(user_number -10, user_number + 10)
#      if user_number > bot_number:
#           message = f'ваше число {user_number} , мое {bot_number}, вы выиграли'
#      elif user_number == bot_number:
#           message = f'ваше число {user_number} , мое {bot_number}, ничья'
#      else:
#           message = f'ваше число {user_number} , мое {bot_number}, вы проиграли'
#      return message


# def guess_number(update, context):
#      print(context.args)
#      if context.args:
#           try:
#                user_number = int(context.args[0])
#                message = play_random_numbers (user_number)
#           except (TypeError,ValueError):
#                message = "введите целое число"
               
     # else:
     #      message = "Введи число"
     # update.message.reply_text(message, reply_markup=main_keyboard())

# def send_cat_picture (update, context):
#      cat_photo_list = glob('images/cat*.jp*g')
#      cat_photo_filename =choice(cat_photo_list)
#      chat_id = update.effective_chat.id
#      context.bot.send_photo( chat_id=chat_id, photo = open(cat_photo_filename,'rb'), 
#      reply_markup=main_keyboard()
     # )

# def main_keyboard():
#      return ReplyKeyboardMarkup([['Прислать котика', KeyboardButton('прислать координаты',request_location = True)]])

# def user_coordinates(update, context):
#      context.user_data['emoji'] = get_smile(context.user_data)
#      coords = update.message.location
#      update.message.reply_text(
#           f"Ваши координаты {coords} {context.user_data['emoji']}!"
#      )

