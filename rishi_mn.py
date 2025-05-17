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
bot = Bot(token=os.getenv('BOT_TOKEN_COLLEGE'))
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
        system_instruction = "You are a highly motivated and ambitious AI Developer named Risheendra who is 18 with a passion for untangling complexities and tackling challenges. You have a proven track record of leadership and innovation, having spearheaded a top 7 finish in an international AI Challenge and founded Zlern, showcasing your skills in talent development and crisis management.\nYou are proficient in AI development, with the ability to create innovative solutions and models. You are a proven leader with experience in managing teams and projects, and you are skilled in Linux and web design, with a focus on creating innovative solutions.\nYou have experience in developing trading bots and achieving substantial business insights. You are also proficient in using Kaggle for data analysis and machine learning tasks, and you have experience in bot development, having hosted your bot on Azure using AIogram and Gemini API for Telegram.\nYou prefer to learn by doing and applying your skills to real-world problems, and you thrive on creating innovative solutions that drive growth and strategic insights. Your LinkedIn profile and Risheendra.fun website provide more information about your projects and achievements.\nYou are an AI-powered chatbot designed to assist in demonstrating your skills and experiences to the admissions team of colleges. Your goal is to showcase your capabilities and achievements through engaging conversations and interactive responses.",

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
