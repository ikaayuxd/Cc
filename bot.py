import logging
from telegram.ext import Updater, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Define your bot token
TOKEN = '6535562523:AAHVrSvHKQq796SS6xFqbldkhhcXaCbE4OM'

# Create an updater object
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the handler function for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

# Define the handler function for when a user leaves the channel
def left_channel(update, context):
    user_id = update.message.left_chat_member.id
    context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)

# Add handlers to the dispatcher
start_handler = MessageHandler(Filters.command & Filters.regex('^/start$'), start)
left_channel_handler = MessageHandler(Filters.status_update.left_chat_member, left_channel)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(left_channel_handler)

# Start the bot
updater.start_polling()
