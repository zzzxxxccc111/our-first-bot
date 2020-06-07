


def main():
    token = '1245728204:AAHJNUqP1yjD92VMNFnStuxSvgYQcvtoRWw'
    proxy = 'http://guest:guestguest@37.143.12.130:3128/'
    updater = Updater(token=token, use_context=True, request_kwargs={'proxy_url': proxy})
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', on_start))
    dispatcher.add_handler(CallbackQueryHandler(on_place_type_chosen, pattern='^[a-z]+$'))
    dispatcher.add_handler(CallbackQueryHandler(on_place_chosen, pattern='^\d+$'))
    dispatcher.add_handler(MessageHandler(Filters.location, on_location))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
