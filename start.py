import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

openai.api_key = 'chatgpt-key'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a ChatGPT bot. How can I help you?")

def chat(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,presence_penalty=0
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

def main():
    updater = Updater('telegram-key', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))
    updater.start_polling()
    #updater.idle()

if __name__ == '__main__':
    main()
