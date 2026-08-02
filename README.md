# LinkMind_AI

###### About the project 


1. The user pastes the link of webpage then AI agent will go through the webpage and extract the content using BeautifulSoup (used for scrapping), It uses NLP spacy is used to extract keywords to understand the context mainly meant for categorizing bookmark and store it in Database

2. we use streamlit for creating UI, also bcrypt lib is used in case of authentication of passwords and user mail or email id.

3. It is also equipped with Groq LLM for providing recommended suggestions.

4. Build a docker image as attached in file slight change is made in the mongodb, database name and ollama model they should be available during the runtime

###### popular commands in cmd 

1. pip install -r requirements.txt
2. python -m venv venv
3. streamlit run <app>.py
4. docker run -p 8501:8501 -e GROQ_API_KEY="<API Key name>" bookmark-ai

##### dependencies needed

1. python version 11 or above (version 11 is recommended)
2. requirements.txt
3. Vs code


# Output

#### UI

1. <img width="1917" height="1079" alt="image" src="https://github.com/user-attachments/assets/ecf5c117-f193-4761-a627-3a6a9ce11f6f" />

2. <img width="1836" height="860" alt="image" src="https://github.com/user-attachments/assets/b5496248-1acb-428d-9f78-bfbb6a3b9fe4" />

3. <img width="1919" height="869" alt="image" src="https://github.com/user-attachments/assets/19e51ddc-f721-4713-87ce-7cbf573c79ba" />

4. <img width="1916" height="948" alt="image" src="https://github.com/user-attachments/assets/95b29f6d-f04f-43e3-908b-2c13dac9cc39" />

5. <img width="1892" height="694" alt="image" src="https://github.com/user-attachments/assets/8ec93436-7f1f-4f74-9773-ea3ce8a8634b" />

6. <img width="1909" height="890" alt="image" src="https://github.com/user-attachments/assets/f007b3b9-0028-413e-96b9-5f20a102fccd" />

7. <img width="1500" height="768" alt="image" src="https://github.com/user-attachments/assets/9c4d385e-f726-4fc5-9652-a3aeeed3ab00" />

8. <img width="1542" height="826" alt="image" src="https://github.com/user-attachments/assets/982b66ea-06bf-4a64-874c-6fcb0c43bc43" />

9. <img width="1598" height="825" alt="image" src="https://github.com/user-attachments/assets/3881630f-d663-4960-bc40-4d97e4193d6f" />



#### DataBase (Mongodb images)

1. <img width="1447" height="676" alt="image" src="https://github.com/user-attachments/assets/9ba8fe9f-7523-40c4-b0ed-79ccf33f7d21" />

2. <img width="1457" height="720" alt="image" src="https://github.com/user-attachments/assets/919d97b3-d3c1-41fd-b8d1-0fd34d075897" />

3. <img width="1468" height="753" alt="image" src="https://github.com/user-attachments/assets/a86dc93a-7c1a-4fa9-aee0-65df4e0a848d" />




