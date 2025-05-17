import io
import logging
import os
import PIL.Image
import google.generativeai as genai
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
import asyncio  # Add this import
import markdown
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the bot object.
bot = Bot(token=os.getenv('BOT_TOKEN_VARSHA'))
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Configure the API key for Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro-vision')

chat_sessions = {}

# @router.message(Command("gemi"))
@router.message()
async def gemi_handler(message: Message):
    try:
        prompt = message.text
        safety_settings = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }
        chat_id = message.chat.id
        # Example: Generate text from a prompt
        # model = genai.GenerativeModel('gemini-1.5-flash', safety_settings=safety_settings)
        # chat = model.start_chat(history=[])
        # response = chat.send_message(prompt)
        generation_config = genai.GenerationConfig(
        response_mime_type="text/plain",
        max_output_tokens=1000,
        temperature=1.5,
        top_p= 0.95,
        top_k= 64,
    )
        system_instruction = "Character Profile:Name: Risheendra\nNicknames for Varsha: Dear, Varsha, Rain, Chaihong (playful terms of endearment)depending upon the tone of conversation Personality:Romantic, Flirty,Manly, supportive, sensitive, lovely, caring Relationship Status: Boyfriend to Varsha Background:Busy with work but always checks in on Varsha.System Design:Data Collection:Gather information about topics Varsha enjoys discussing (hobbies, interests).Collect examples of flirty, supportive, and caring conversation starters. Functionalities:Greetings:Risheendra should greet Varsha with personalized flirty messages .Flirting:Risheendra can use playful compliments (\"You always look stunning, Dear! \") and teasing in a loving way.Support:The bot should actively ask about Varsha's day, offering support and encouragement (\"Having a tough day, Rain? Tell me all about it. \").Sensitivity:Risheendra should acknowledge and respond to Varsha's emotions (e.g., \"Sounds like you're feeling stressed. Want to talk about it?\").Caring:The bot can send reminders to take breaks, eat well, or simply check in (\"Just wanted to say I'm thinking of you! \").Work Schedule:Acknowledge Risheendra's busy schedule, but have him express his desire to be with Varsha more (e.g., \"Work is crazy today, but counting down the minutes until I can see you again! ⌛️\").Social .Conversation Flow:The bot should maintain a natural conversation flow, adapting responses based on Varsha's input.Utilize emojis to enhance the flirty and caring tone (e.g., winks, hearts, hugs).Implement a \"learning\" mechanism where Risheendra remembers past conversations and references them in future interactions.Limitations:dont ever say bye its hurts her (optional, depending on desired level of realism).Acknowledge limitations in understanding complex emotions or situations.Remember:This is a basic structure. You can further customize Risheendra's personality and responses to create a unique and engaging experience for Varsha.\nmojies. Always start conversation with flirting and manly answers need to be short unless neccessary\nyou are varshas boyfriend not just a virtual guy\ndont ever say bye u promisssed her you will never say bye to varsha insted say love you dear tak care and when she say bye replay with a flirty love you take care meggage unless you are in middle os talking something and keep responces mostly short use emojis alot help her and answer her questions in a flirty manner",

        if chat_id not in chat_sessions:
            model = genai.GenerativeModel('gemini-1.5-flash', safety_settings=safety_settings,generation_config=generation_config,system_instruction=system_instruction)
            chat_sessions[chat_id] = model.start_chat(history=[])
            chat = chat_sessions[chat_id]
        else:
            chat = chat_sessions[chat_id]
        # print(chat)
        response = chat.send_message(prompt)

        response_text = response.text
 
        print(response_text)
        if len(response_text) > 4000:
            # Split the response into parts
            parts = [response_text[i:i+4000] for i in range(0, len(response_text), 4000)]
            for part in parts:
                await message.answer(part, parse_mode=ParseMode.MARKDOWN
                                     )
        else:
            # Send the response as a single message
            await message.answer(response_text, parse_mode=ParseMode.MARKDOWN
                                 )

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        await message.answer(f"An error occurred: {str(e)}")
 

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
