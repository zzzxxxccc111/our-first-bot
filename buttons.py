

def on_start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Рестораны", callback_data='restaurants'),
            InlineKeyboardButton("Клубы", callback_data='clubs')
        ],
        [
            InlineKeyboardButton("Кино", callback_data='cinema'),
            InlineKeyboardButton("Парки", callback_data='park')
        ],
        [
            InlineKeyboardButton("Бары", callback_data='bar'),
            InlineKeyboardButton("Театры", callback_data='theatre')
        ]
    ]

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Куда вы хотите сходить?',
                             reply_markup=InlineKeyboardMarkup(keyboard))


