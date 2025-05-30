import json
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_intent(file_type, content):
    if isinstance(content, dict):
        content_str = json.dumps(content, indent=2)  # Convert dict to string
    else:
        content_str = str(content)

    prompt = f"Classify the intent of this {file_type} content:\n{content_str[:1000]}\nIntent:"


    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=20
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Unknown"
