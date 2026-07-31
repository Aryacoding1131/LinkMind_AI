from langchain_ollama import ChatOllama
from config.settings import OLLAMA_MODEL
import json
import re


llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0
)



def classify_website(text):

    prompt = f"""

You are a website classifier.

Classify this webpage.

Choose only one category:

Programming
Artificial Intelligence
Machine Learning
Data Science
Education
Technology
Business
Finance
Healthcare
News
Sports
Travel
Gaming
Entertainment
Cooking
Shopping
Research
Others


Return ONLY JSON.

Format:

{{
"category":"Technology",
"confidence":90,
"tags":["tag1","tag2","tag3"]
}}


Content:

{text[:4000]}

"""


    try:

        response = llm.invoke(prompt)


        output = response.content.strip()


        # Remove markdown JSON blocks

        output = output.replace(
            "```json",
            ""
        )

        output = output.replace(
            "```",
            ""
        )


        # Extract JSON object

        match = re.search(
            r"\{.*\}",
            output,
            re.DOTALL
        )


        if match:

            json_text = match.group()

            result = json.loads(json_text)


            return result


        else:

            return {

                "category":"Others",

                "confidence":0,

                "tags":[]

            }


    except Exception as e:


        return {

            "category":"Others",

            "confidence":0,

            "tags":[],

            "error":str(e)

        }
