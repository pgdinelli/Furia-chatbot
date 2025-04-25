from dotenv import load_dotenv
from openai import OpenAI
import os

# carregando variáveis dotenv para consumir a API da LM Studio
load_dotenv()

# fazendo conexão do LM Studio com a API da OpenAI
client = OpenAI(
    base_url = os.getenv("LM_STUDIO_URL"), api_key="lm-studio"
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
    
    # retornando requisições HTTP da API da OpenAI
    return response.choices[0].message.content

user_input = input("Digite aqui sua mensagem: ")
bot_response = send_messages(user_input)
print("Chatbot: ", bot_response)