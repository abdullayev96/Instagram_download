from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton



Token = "6895917982:AAGJl8FZPiaUTPsP2eyJdiUtf_9QdwLU87g"




questions = [
    {"Savol":"1-Eng mashhur tillarni ayting",
     "javob":"a",
     "a":"Python, java, javascript",
     "b":"Php, Go, C++",
     "d":"Ardinou, Django",
     "c":"a va b togri"
     },
    {"Savol":"2-Eng oson  tillarni ayting",
     "javob":"a",
     "a":"Python javascript",
     "b":"Php, Go",
     "d":"Ardinou, Django",
     "c":"a va b togri"
    },
    {"Savol": "3-Eng qiyin  tillarni ayting",
     "javob": "b",
     "a": "Python, Java",
     "b": "C++, Go",
     "d": "Ardinou,C",
     "c": "a va b to\'gri"
     },
    {"Savol": "4-Eng Kotta conpaniyalrni  ayting",
     "javob": "c",
     "a": "Geogle, epam",
     "b": "Pdp, Golong",
     "d": "Anaconda, Facebook",
     "c": "a va d to\'gri"
     },
    {"Savol": "5-Eng Kotta daryoni  ayting",
     "javob": "a",
     "a": "Amazonka",
     "b": "Nil",
     "d": "Sirdaryo",
     "c": "Amudaryo"
     },

]



def start_command(update, context):
    global questions
    buttons  = [
        [InlineKeyboardButton(text=f"{questions[0]['a']}", callback_data='a')],   ##### new 1
        [InlineKeyboardButton(text=f"{questions[0]['b']}", callback_data='b')],
        [InlineKeyboardButton(text=f"{questions[0]['c']}", callback_data='c')],
        [InlineKeyboardButton(text=f"{questions[0]['d']}", callback_data='d')],
    ]
    context.user_data['question_id'] = 0
    context.user_data['answers'] = []


    update.message.reply_text(
        text=f"{questions[0]['Savol']}",
        reply_markup=InlineKeyboardMarkup(buttons))




def message_handler(update, context):

    update.message.reply_text(
        text="Hello welcome!!!"
    )
    if context.user_data.get("text"):
        words=context.user_data.get("text")
    else:
        words=[]
    words.append(update.message.text)
    context.user_data['text']=words
    print(context.user_data.get("text"))



def inline_handler(update, context):
    global  questions
    query = update.callback_query

    if query.data in ['a', 'b', 'c', 'd']:     ####   new 2



        question_id = context.user_data.get('question_id', 0)  ### new 3
        if question_id < len(questions) - 1:  #### new 4
            buttons = [
                [InlineKeyboardButton(text=f"{questions[question_id + 1]['a']}", callback_data='a')],
                [InlineKeyboardButton(text=f"{questions[question_id + 1]['b']}", callback_data='b')],
                [InlineKeyboardButton(text=f"{questions[question_id + 1]['c']}", callback_data='c')],
                [InlineKeyboardButton(text=f"{questions[question_id + 1]['d']}", callback_data='d')],
            ]
            query.message.edit_text(text = f"{questions[question_id + 1]['Savol']}",  ######  5
            reply_markup = InlineKeyboardMarkup(buttons)
            )
            context.user_data['question_id'] = question_id + 1    #####  6
        else:
            query.message.reply_text("Test tugadi")




updater = Updater(Token, request_kwargs={'read_timeout': 10, 'connect_timeout': 10})
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
dispatcher.add_handler(CallbackQueryHandler(inline_handler))

updater.start_polling()