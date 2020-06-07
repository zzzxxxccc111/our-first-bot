def on_place_type_chosen(update, context):
    query = update.callback_query
    query.answer()

    context.user_data['place_type'] = query.data
    context.bot.send_message(chat_id=update.effective_chat.id, text='Где мне искать?')


def on_place_chosen(update, context):
    query = update.callback_query
    query.answer()

    place_id = query.data
    response = requests.get(f'https://kudago.com/public-api/v1.4/places/{place_id}/?lang=en')
    data = response.json()

    title = data['title']
    address = data['address']
    timetable = data['timetable']
    description = re.sub('<[^<]+?>', '', data['description'])






   