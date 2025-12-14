from dotenv import load_dotenv

load_dotenv()

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = "Explain the concept of 'LOVE' in one sentence"

temperatures = [0.1, 0.5, 1.0]

print("Prompt: " + prompt + "\n")

for temp in temperatures:
    generation_config = genai.types.GenerationConfig(
        temperature=temp
    )

    response = model.generate_content(
        prompt, 
        generation_config=generation_config
    )

    print(f'<--- Temprature {temp} --->')
    print(f'{response.text.strip()}\n')