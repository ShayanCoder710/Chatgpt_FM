import telebot
from openai import OpenAI


token = "token"
api_key = "api_key"


client = OpenAI(base_url ='https://api.gapgpt.app/v1',api_key=api_key)


bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def start(message):
    bot.reply_to(message , "سلام ربات هوش مصنوعی chatgpt_FM فعال شد🤖\nهر سوالی دارید بپرسید")


@bot.message_handler(func=lambda m : True)
def reply(message):
    user_text = message.text


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role" : "user", "content" : user_text}]
    )


    ai_answer = response.choices[0].message.content
    bot.reply_to(message , ai_answer)



bot.polling()
