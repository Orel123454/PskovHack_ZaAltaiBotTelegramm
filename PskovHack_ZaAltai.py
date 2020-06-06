import telebot
import feedparser
import random
from telebot import types

python_wiki_rss_url= "https://news.yandex.ru/koronavirus.rss"   # Ссылка на rss новости, возможны любые новости в формате rss

feed = feedparser.parse( python_wiki_rss_url )

bot = telebot.TeleBot('Токин съели конспирологи:(((') # Авторизируемся через токин бота
summ = 0
ft = []
for post in feed.entries:
    ft.append(post.title + "\n" + post.description + "\n" + post.link) # Разбиваем ленту на новости
  

@bot.message_handler(content_types=['text']) # Включаем прослушивание текстовых сообщений
def start(message):
    keyboard = types.InlineKeyboardMarkup()  # Создаём клавиатуру
    key_yes = types.InlineKeyboardButton(text='Новости', callback_data='new') 
    keyboard.add(key_yes); 
    question = "Что Вы хотите от такого милого бота?" + "\n" + "Вы можете:" + "\n" + "Посмотреть голосования"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard) 
    

@bot.callback_query_handler(func=lambda call: True) # Прослушивание данных с клавиатуры
def callback_worker(call):
    global summ
    if call.data == "new": 
        bot.send_message(call.message.chat.id, ft[random.randint(0, 5)]) # Вывод новостей. 5 указывается для избежения нехватки новостей
        keyboard = types.InlineKeyboardMarkup()  # Создаём клавиатуру
        key_yes = types.InlineKeyboardButton(text='Согласен', callback_data='yes') 
        keyboard.add(key_yes); 
        key_no = types.InlineKeyboardButton(text='Против', callback_data='no') 
        keyboard.add(key_no); 
        question = "Проголосуйте за данную инициативы, вы за или против?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data =="yes":
        bot.send_message(call.message.chat.id, ft[random.randint(0, 5)]) # Вывод новостей. 5 указывается для избежения нехватки новостей
        keyboard = types.InlineKeyboardMarkup()  # Создаём клавиатуру
        key_yes = types.InlineKeyboardButton(text='Согласен', callback_data='yes') 
        keyboard.add(key_yes); 
        key_no = types.InlineKeyboardButton(text='Против', callback_data='no') 
        keyboard.add(key_no); 
        question = "Проголосуйте за данную инициативы, вы за или против?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, ft[random.randint(0, 5)]) # Вывод новостей. 5 указывается для избежения нехватки новостей
        keyboard = types.InlineKeyboardMarkup()  # Создаём клавиатуру
        key_yes = types.InlineKeyboardButton(text='Согласен', callback_data='yes') 
        keyboard.add(key_yes); 
        key_no = types.InlineKeyboardButton(text='Против', callback_data='no') 
        keyboard.add(key_no); 
        question = "Проголосуйте за данную инициативы, вы за или против?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)


bot.polling(none_stop=True, interval=0) # Пуллинг 