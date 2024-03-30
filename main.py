import requests
from dotenv import load_dotenv
import os
from send_email import send_email

load_dotenv()
api_key = os.getenv('API_KEY')
url = 'https://newsapi.org/v2/everything?q=tesla&' \
    'from=2024-02-29&sortBy=publishedAt&apiKey=24001234ba4f4bfeaf484ce8137fe68b'

req = requests.get(url)
content = req.json()

email = ''
for i, article in enumerate(content['articles']):
    email += f'''{i+1}
    {article['title']}
    {article['description']}

    '''

email = email.encode('utf-8')
send_email(email)
