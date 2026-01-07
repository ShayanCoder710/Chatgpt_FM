from rubka.asynco import Robot, Message, filters
from openai import OpenAI
import asyncio


token = "token"
api_key = "api_key"


client = OpenAI(base_url ='https://api.gapgpt.app/v1',api_key=api_key)


bot = Robot(token)
print("""
      

 __  __  ___  _   _    _    __  __ __  __    _    ____  _ ____  ____   ___  
|  \/  |/ _ \| | | |  / \  |  \/  |  \/  |  / \  |  _ \(_)  _ \|___ \ / _ \ 
| |\/| | | | | |_| | / _ \ | |\/| | |\/| | / _ \ | | | | | |_) | __) | | | |
| |  | | |_| |  _  |/ ___ \| |  | | |  | |/ ___ \| |_| | |  _ < / __/| |_| |
|_|  |_|\___/|_| |_/_/   \_\_|  |_|_|  |_/_/   \_\____/|_|_| \_\_____|\___/ 



      By Mohammadir20💙
      """)



@bot.on_message(filters=filters.text_equals("/start"))
async def start_dege_zayas(_: Robot, message: Message): 

    await message.reply("سلام ربات هوش مصنوعی chatgpt_FM فعال شد🤖\nهر سوالی دارید بپرسید")
    

@bot.on_message()
async def ai_response(_: Robot, message: Message):
    user_text = message.text


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role" : "user", "content" : user_text}]
    )


    ai_answer = response.choices[0].message.content
    await message.reply(ai_answer)



if __name__ == "__main__":
    asyncio.run(bot.run())
