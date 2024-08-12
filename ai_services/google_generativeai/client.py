
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

def get_car_ai_bio_google(model, brand, year) -> str:
    prompt = '''
      Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres.
    '''
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt.format(brand, model, year))
    return response.text
