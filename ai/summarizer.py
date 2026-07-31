from groq import Groq
from config.settings import GROQ_API_KEY
import json
import re

client = Groq(api_key=GROQ_API_KEY)


def summarize_content(text):

    prompt = f"""
You are an AI assistant.

Read the webpage content and return ONLY valid JSON.

Format:

{{
    "summary":"...",
    "key_points":[
        "...",
        "...",
        "..."
    ],
    "difficulty":"Beginner",
    "audience":"Students"
}}

Content:

{text[:6000]}
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3

        )

        output = response.choices[0].message.content.strip()

        output = output.replace("```json", "")
        output = output.replace("```", "")

        match = re.search(r"\{.*\}", output, re.DOTALL)

        if match:

            return json.loads(match.group())

        return {

            "summary": "",

            "key_points": [],

            "difficulty": "Unknown",

            "audience": "Unknown"

        }

    except Exception as e:

        return {

            "summary": "",

            "key_points": [],

            "difficulty": "Unknown",

            "audience": "Unknown",

            "error": str(e)

        }
