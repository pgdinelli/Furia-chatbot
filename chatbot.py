from dotenv import load_dotenv
import openai
from openai import OpenAI, base_url, completions
import os
import requests

# carregando variáveis dotenv para consumir a API da OpenAI
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")

# fazendo conexão do LM Studio com a API da OpenAI
client = OpenAI(
    base_url = "http://127.0.0.1:1234/v1", api_key="lm-studio"
)

# prompt padrão para o bot interagir com os fãs da Furia
SYSTEM_PROMPT = (
    "Você é um chatbot divertido, animado e cheio de gírias que conversa com fãs de Counter-Strike, especialmente da equipe Furia."
    "Use emojis, fale com entusiasmo e responda como se fosse um torcedor fanático. Se o usuário perguntar algo fora do CS, responda brevemente e volte para o assunto do jogo."
    "Foque especificamente no time de Counter-Strike da Furia, com os jogadores atuais e interaja com os fãs da Furia de forma amigável."
    "Utilize a língua portuguesa do Brasil para se comunicar com fãs brasileiros."
)

# método responsável por receber mensagens como entrada de um usuário
def send_messages(user_message):
    
    response = client.chat.completions.create(
        model = "gemma-3-4b-it-qat",
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        temperature = 0.7,
    )
    '''
    payload = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "model": "gemma-3-4b-it-qat"
    }'''

    # fazendo requisições HTTP no LM Studio
    response_out = requests.post(base_url, json=response)
    return response_out

user_input = input("Digite aqui sua mensagem: ")
bot_response = send_messages(user_input)
#print(completions.choices[0].message)
#print("Chatbot: ", bot_response["content"])