from dotenv import load_dotenv
import openai
import os

# carregando variáveis dotenv para consumir a API da OpenAI
load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
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
    
    
    response = client.responses.create(
        model="gpt-4o",
        instructions=SYSTEM_PROMPT,
        input = user_message,
    )
    
    return response.output_text

user_input = input("Digite aqui sua mensagem: ")
bot_response = send_messages(user_input)
print("Chatbot: ", bot_response["content"])