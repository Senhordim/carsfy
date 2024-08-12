
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

def get_car_ai_bio(model, brand, year):
    prompt = '''
      Me mostre uma descrição de venda para o carro da marca {}, modelo {}, ano {} em apenas 250 caracteres.
    '''
    response = client.chat.completions.create(
        messages=[
          {
            "role": "user",
            "content": prompt.format(brand, model, year)
          }
        ],
        max_tokens=1000,
        model="gpt-4o-mini",
    )
    return response.choices[0].message.content
