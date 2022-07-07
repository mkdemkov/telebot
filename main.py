import time

import telebot
from telebot import types
import math

global count_yes, count_no, count_yes_no
global chat_id
global ind
global ind_girl

bot = telebot.TeleBot('5501458544:AAFN8ZZP5xIACExlA4wyreHD7recnuI1STE')

quest = ["Есть ли у тебя друзья?", "Появляется ли на твоём лице улыбка, когда ты смотришь на мужчин?",
         "Часто ли ты засматриваешься на мужчин, когда едешь на работу/учёбу?",
         "Хотел ли бы ты тройничёк с мужчиной и красивой девушкой?", "Часто ли ты говоришь комплименты мужчинам?",
         "Представлял ли ты мужчину в своей сексуальной фантазии?",
         "Думал ли ты, что можешь полностью отказаться от общения с мужчинами?",
         "Считаешь ли ты сумасшедшими людей, которые ущемляют права мужчин?"]

quest_girl = ["Есть ли у тебя подруги?", "Появляется ли у тебя улыбка на лице, когда ты смотришь на девушку?",
              "Часто ли ты засматриваешься на девушек, когда едешь на работу/учёбу?",
              "Хотела бы ты тройничёк с красивой девушкой и мужчиной?", "Часто ли ты говоришь девушкам комплименты?",
              "Представляла ли ты девушку в своей сексуальной фантазии?",
              "Думала ли ты, что можешь прекратить общение с девушками?",
              "Считаешь ли ты сумасшедшими людей, которые ущемляют права женщин?"]


@bot.message_handler(commands=['about'])
def about(message):
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Я - бот🤖, позволяющий проверить насколько ты гомосексуален(или склонна к лесбиянству)\n\n"
                     "Моего создателя можно найти, отсканировав следующий QR-код:")
    qr_code = open('data/t_me-filledevoler.jpg', 'rb')
    bot.send_photo(chat_id, qr_code)


@bot.message_handler(commands=['start'])
def start(message):
    global chat_id
    chat_id = message.chat.id
    global count_yes, count_no
    global ind
    global ind_girl
    count_yes = count_no = 0
    ind = 0
    ind_girl = 0

    bot.send_message(chat_id,
                     f'<b>Приветствую, ❤️{message.from_user.first_name}❤️!</b>\n' + 'Если ты решил(а) воспользоваться '
                                                                                    'этим ботом, '
                                                                                    'значит тебе интересна твоя '
                                                                                    'ориентация 👻\n',
                     parse_mode='HTML')
    show_button(message)


def show_button(message):
    global chat_id
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Я парень👦🏻")
    btn2 = types.KeyboardButton("Я девушка👩🏼")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "Для начала давай определимся с полом:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def parse_user_text(message):
    global count_yes, count_no, count_yes_no
    global chat_id
    chat_id = message.chat.id
    if message.text == "Я парень👦🏻":
        bot.send_message(chat_id, "<b>Ну что, сладкий, поехали!</b>", parse_mode="HTML")
        first_quest(message)
    elif message.text == "Я девушка👩🏼":
        bot.send_message(chat_id, "<b>Ну что, сладкая, поехали!</b>", parse_mode="HTML")
        first_quest_girl(message)
    elif message.text == "А":
        bot.send_message(chat_id, f"{count_yes} {count_no}")
    elif message.text == "Big Fat Cock":
        bot.send_message(chat_id, "<b>Поздравляю! У вас реально big fat cock!</b>", parse_mode="HTML")
    else:
        bot.send_message(chat_id, "Я не могу обработать такое сообщение 😢")


def first_quest(message):
    global ind
    global chat_id
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Да👍🏻", callback_data="yes")
    btn2 = types.InlineKeyboardButton("Нет👎🏻", callback_data="no")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, quest[ind], reply_markup=markup)


def first_quest_girl(message):
    global chat_id
    global ind
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Yes👍🏻", callback_data="da")
    btn2 = types.InlineKeyboardButton("No👎🏻", callback_data="net")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, quest_girl[ind], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_da(call):
    global chat_id
    global count_yes
    global count_no
    global ind
    if call.message:
        if call.data == "da":
            show_answer_res("")
            count_yes += 1
            ind += 1
            if ind >= len(quest_girl):
                final_quest_girl()
            else:
                send_girl(quest_girl[ind])
        elif call.data == "net":
            show_answer_res("")
            count_no += 1
            ind += 1
            if ind >= len(quest_girl):
                final_quest_girl()
            else:
                send_girl(quest_girl[ind])


        elif call.data == "first":
            bot.send_message(chat_id, "Какая ты умничка! Не предала свою подружку, горжусь тобой❤️")
            sticker = open('data/momhave.webp', 'rb')
            bot.send_sticker(chat_id, sticker)
            beatiful_download()
            func_end_girl()

        elif call.data == "second":
            bot.send_message(chat_id, "Вот ты сука! Променяла подругу на мужчину...гадость🤢")
            sticker = open('data/momless.webp', 'rb')
            bot.send_sticker(chat_id, sticker)
            beatiful_download()
            func_end_girl()

        else:
            if call.data == "yes":
                show_answer_res("Да")
                count_yes += 1
                # global ind
                ind += 1
                if ind >= len(quest):
                    final_quest()
                else:
                    send(quest[ind])
            elif call.data == "no":
                # elif call.data == "no":
                show_answer_res("Нет")
                count_no += 1
                ind += 1
                if ind >= len(quest):
                    final_quest()
                else:
                    send(quest[ind])
            else:
                if call.data == "girl":
                    bot.send_message(chat_id, "Ах ты сука-то такая! Кента на женщину променял! Фу!")
                    stick = open('data/sticker.webp', 'rb')
                    bot.send_sticker(chat_id, stick)
                    bot.send_message(chat_id, "Не очень хочется продолжать с тобой дискуссию, но вот твой результат⚡️")
                    beatiful_download()
                    func_end()
                    # МБ НИЖЕ КРАШ
                elif call.data == "boy":
                    bot.send_message(chat_id, "Хорош! Тест на п#дора прошёл! Кенты могут тобой гордиться")
                    stick = open('data/sticker_good.webp', 'rb')
                    bot.send_sticker(chat_id, stick)
                    beatiful_download()
                    func_end()


def send_girl(message):
    global chat_id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Yes👍🏻", callback_data="da")
    btn2 = types.InlineKeyboardButton("No👎🏻", callback_data="net")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, message, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_yes(call):
    global chat_id
    global count_yes
    global count_no
    global ind
    if call.message:
        if call.data == "yes":
            show_answer_res("Да")
            count_yes += 1
            # global ind
            ind += 1
            if ind >= len(quest):
                final_quest()
            else:
                send(quest[ind])
        elif call.data == "no":
            # elif call.data == "no":
            show_answer_res("Нет")
            count_no += 1
            ind += 1
            if ind >= len(quest):
                final_quest()
            else:
                send(quest[ind])
        else:
            if call.data == "girl":
                bot.send_message(chat_id, "Ах ты сука-то такая! Кента на женщину променял! Фу!")
                stick = open('data/sticker.webp', 'rb')
                bot.send_sticker(chat_id, stick)
                bot.send_message(chat_id, "Не очень хочется продолжать с тобой дискуссию, но вот твой результат⚡️")
                beatiful_download()
                func_end()
                # МБ НИЖЕ КРАШ
            elif call.data == "boy":
                bot.send_message(chat_id, "Хорош! Тест на п#дора прошёл! Кенты могут тобой гордиться")
                stick = open('data/sticker_good.webp', 'rb')
                bot.send_sticker(chat_id, stick)
                beatiful_download()
                func_end()


def send(message):
    # bot.send_message(chat_id, message)
    global chat_id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Да👍🏻", callback_data="yes")
    btn2 = types.InlineKeyboardButton("Нет👎🏻", callback_data="no")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, message, reply_markup=markup)


def show_answer_res(answer):
    global chat_id
    bot.send_message(chat_id, "-----------------------------------------")


def final_quest():
    global chat_id
    bot.send_message(chat_id, "<b>Итак, финальный вопрос❗</b>️", parse_mode="HTML")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Подругу🧍🏼‍♀️", callback_data="girl")
    btn2 = types.InlineKeyboardButton("Друга🧍🏻", callback_data="boy")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "Тебя зовут гулять друг и подруга. Кого ты выберешь?", reply_markup=markup)


def final_quest_girl():
    global chat_id
    bot.send_message(chat_id, "Внимание! послоедний вопрос")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Подругу💃🏻️", callback_data="first")
    btn2 = types.InlineKeyboardButton("Друга🕺🏻", callback_data="second")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "Тебя зовёт гулять подруга и друг. Кого ты выберешь?", reply_markup=markup)


def func_end():
    global count_yes, count_no
    global chat_id
    final_res = round(count_yes / 8 * 100)
    bot.send_message(chat_id, f"Вы гомосексуальны на <b>{final_res}%</b>", parse_mode="HTML")
    if final_res > 80:
        bot.send_message(chat_id, "Поздравляю! В этой жизни нет ничего лучше, чем мужчина нетрадиционных взглядов😘")
        audio = open('data/Oleg_Gazmanov_-_Moi_yasnye_dni_right_version_Gachi_Remix_69147154.mp3', 'rb')
        bot.send_audio(chat_id, audio)
    elif final_res > 50:
        bot.send_message(chat_id,
                         "Вижу, что ты находишься на переплетении судьбы. Надеюсь, дальше ты будешь двигаться в "
                         "правильном направлении, if you know what I mean🏳️‍🌈😉")
    else:
        bot.send_message(chat_id,
                         "Что ж, вижу ты традиционных взглядов. Ничего не сказать, твой выбор. Спасибо,"
                         " что воспользовался ботом💀")


def func_end_girl():
    global count_yes, count_no
    global chat_id
    final_res = round(count_yes / 8 * 100)
    bot.send_message(chat_id, f"Вы лесбиянка на <b>{final_res}%</b>", parse_mode="HTML")
    if final_res > 80:
        bot.send_message(chat_id, "Поздравляю! В этой жизни нет ничего лучше, чем девушки, любящие других девушек😘")
    elif final_res > 50:
        bot.send_message(chat_id,
                         "Вижу, что ты находишься на переплетении судьбы. Надеюсь, дальше ты будешь двигаться в "
                         "правильном направлении, if you know what I mean🏳️‍🌈😉")
    else:
        bot.send_message(chat_id,
                         "Что ж, вижу ты традиционных взглядов. Ничего не сказать, твой выбор. Спасибо,"
                         " что воспользовалась ботом💀")


def beatiful_download():
    global chat_id
    down = bot.send_message(chat_id, "<b>Результаты появятся через 3</b>", parse_mode="HTML")
    time.sleep(2)
    bot.edit_message_text(chat_id=chat_id, message_id=down.id, text="<b>Результаты появятся через 2</b>",
                          parse_mode="HTML")
    time.sleep(2)
    bot.edit_message_text(chat_id=chat_id, message_id=down.id, text="<b>Результаты появятся через 1</b>",
                          parse_mode="HTML")
    time.sleep(2)
    bot.edit_message_text(chat_id=chat_id, message_id=down.id, text="<b>А вот и результат🎉</b>",
                          parse_mode="HTML")


bot.polling(none_stop=True)
