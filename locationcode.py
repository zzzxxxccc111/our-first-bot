


def on_location(update, context):
    location = update.message.location
    context.user_data['lon'] = location.longitude
    context.user_data['lat'] = location.latitude

    params = {'radius': SEARCH_RADIUS_IN_METERS,
              'page_size': 5,
              'categories': context.user_data['place_type'],
              'lon': context.user_data['lon'],
              'lat': context.user_data['lat'],
              'lang': 'en'}

    response = requests.get('https://kudago.com/public-api/v1.4/places/', params=params)
    data = response.json()

    if data['count'] == 0:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Я не смог ничего найти, попробуйте другой адрес')
        return

 