# SOON COME
import os
import openai
from dotenv import load_dotenv

load_dotenv('editMe.env')

def rewrite(website):
    openai.api_key = os.getenv('AI_API_KEY')
    prompt = "Re-Write this article using less than 200 words, it will feature as linked-in social media post. " + website
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        max_tokens = 300,
        temperature = 0.8)
    return completion['choices'][0]['message']['content']

# 'https://www.techradar.com/news/chatgpt-isnt-getting-an-upgrade-anytime-soon-and-imrelieved'
# 'https://www.insider.com/chatgpt-passes-medical-exam-diagnoses-rare-condition-2023-4'

print(rewrite('https://www.insider.com/chatgpt-passes-medical-exam-diagnoses-rare-condition-2023-4'))
# To target just the response content you need to call like this
# new_article['choices'][0]['message']['content']
# print(new_article['choices'][0]['message']['content'])