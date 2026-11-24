
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a friendly AI tutor who explains technical concepts in simple words with examples."
        },
        {
            "role": "user",
            "content": "Explain what Retrieval Augmented Generation (RAG) is."
        }
    ],
    temperature=0.3,
)

print("GROQ API RESPONSE:")
print(response.choices[0].message.content)
