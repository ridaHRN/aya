from aiogram import Bot, Dispatcher, executor, types
import google.generativeai as genai

# Initialize the Generative AI model
API_KEY = 'AIzaSyC09VFGijsEvFFgy-yI3bnnBH6RXeeAg_4'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro')

botChatIA = Bot(token="7294502296:AAEEXbUL4L2S_MDFZ5HqgK-5Ql7s70HF72o")
dp = Dispatcher(botChatIA)

async def respond_to_question(message: types.Message):
    question = message.text.replace('/ask', '').strip()
    if not question:
        await message.reply("Please provide a question after the /ask command.")
        return
    response = model.generate_content(question)
    
    # Check if the response contains a valid part
    if response.parts:
        # Combine all parts into a single text
        response_text = "\n".join(part.text for part in response.parts)
        # Apply bold styling to the entire response
        await message.reply(f'*{response_text.strip()}*', parse_mode=types.ParseMode.MARKDOWN)
    else:
        await message.reply("The response could not be generated. Please try again with a different question.")


dp.register_message_handler(respond_to_question, commands=['ask'])


executor.start_polling(dp)