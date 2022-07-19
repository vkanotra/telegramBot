import auth as auth
from telegram.ext import *
import responses as R

print("Bot started...")


def start_command(update, context):
    update.message.reply_text("Welcome to my bot!")


def help_command(update, context):
    update.message.reply_text("Ask google!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error: {context.error}")


def main():
    updater = Updater(auth.API_auth, use_context= True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()