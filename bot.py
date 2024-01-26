import random
import string
import telegram
from telegram.ext import Updater, CommandHandler

# List of Indian names
names = ['Rahul', 'Deepika', 'Priya', 'Rajesh']

def generate_combinations(update, context):
    # Open a file to save the combinations
    file_name = 'combinations.txt'
    file = open(file_name, 'w')

    for _ in range(10):
        # Randomly select a name and a password
        name = random.choice(names)
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

        # Generate the email combination
        email = f"{name.lower()}@gmail.com:{password}"

        # Write the combination to the file
        file.write(email + '\n')

    # Close the file
    file.close()

    # Send the file to Telegram
    chat_id = update.message.chat_id
    bot = context.bot
    bot.send_document(chat_id=chat_id, document=open(file_name, 'rb'))

    # Delete the file
    os.remove(file_name)

def start(update, context):
    chat_id = update.message.chat_id
    bot = context.bot
    bot.send_message(chat_id=chat_id, text="Bot started. Use /gen to generate email combinations.")

def main():
    # Initialize the Telegram bot
    updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
    dp = updater.dispatcher

    # Add commands handlers
    dp.add_handler(CommandHandler('gen', generate_combinations))
    dp.add_handler(CommandHandler('start', start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
