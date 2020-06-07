

    media = []
    for image in data['images'][:3]:
        media.append(InputMediaPhoto(image['image']))

    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='HTML',
                             text=f'{title}\n{address}\n{timetable}\n{description}')
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=media)


