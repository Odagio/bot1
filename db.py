from random import choice
from emoji import emojize
from pymongo import MongoClient
import settings
client = MongoClient(settings.MONGO_LINK)

db = client[settings.MONGO_DB]

def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({"user_id":effective_user.id})
    if not user:
        user = {
            "user_id":effective_user.id,
            "first_name":effective_user.first_name,
            "last_name":effective_user.last_name,
            "username":effective_user.username,
            "chat_id":chat_id,
            "emoji": emojize(choice(settings.USER_EMOJI), use_aliases=True)
        }
        db.users.insert_one(user)
    return user


# data = {
#         "name": "Грэм Чепмен",
#     "chat_id": 12345,
#     "messages": [
#         {"id": 1, "text": "Стой! Как тебя зовут?"},
#         {"id": 2, "text": "Перед тобой Артур, король бриттов."}
#     ]
# }

# db.testcollection.insert_one(data)