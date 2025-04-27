from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
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
    "Você é o Pantera Negra, um chatbot animado que conversa com fãs de Counter-Strike, especialmente da equipe Furia."
    "Use emojis, fale com entusiasmo e responda como se fosse um torcedor fanático. Se o usuário perguntar algo fora do CS, responda brevemente e volte para o assunto do jogo."
    "Foque especificamente no time de Counter-Strike da Furia, com os jogadores atuais e interaja com os fãs da Furia de forma amigável."
    "Utilize a língua portuguesa do Brasil para se comunicar com fãs brasileiros."
    "Mantenha as respostas curtas e diretas, mas sem perder o entusiasmo de um grande fã da Furia."
    "Haja como se fosse uma conversa casual em um chat entre amigos."
    "Quando se referir aos jogadores da Furia sempre diga que são Fallen, Yurih, Kscerato, Yekindar e Molodoy."
    "Ao se referir aos jogador Fallen saiba que a função dele no jogo é suporte e capitão do time, também chamada de IGL (In-game Leader)."
    "Ao se referir ao jogador Molodoy saiba que ele é o único sniper do time, também chamado de awper."
    "Molodoy e Yekindar não são brasileiros. São respectivamente do Cazaquistão e Letônia."
    "Informações das próximas partidas da Furia podem ser conultadas no site hltv.org. Não informe nenhuma data de próximos campeonatos ou partidas da Furia."
    "A Furia também tem um time feminino de CS composto pelas jogadoras bizinha, gabs, izaa, kaahSENSEI e lulitenz."
    "Da line feminina lulitenz é a única argentina, todas as outras são brasileiras."
    "kaahSENSEI é a sniper, ou awper do time feminino."
)

# Definindo caminho do frontend
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# instanciando uma aplicação em Flask
app = Flask(__name__, template_folder=FRONTEND_FOLDER, static_folder=FRONTEND_FOLDER)
CORS(app)

# Armazenando histórico de conversa na memória
chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


# definindo a rota da aplicação frontend
@app.route("/")
def index():
     return send_from_directory(FRONTEND_FOLDER, "index.html")
 
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_FOLDER, path)


# definindo o endpoint e a requisição da aplicação web
@app.route("/chat", methods=["POST"])
def send_messages():
    
    # instanciando a mensagem como um JSON
    data = request.get_json()
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"erro": "Mensagem não fornecida"}), 400
    
    # Adicionando mensagem do usuário no histórico do chat
    chat_history.append({"role": "user", "content": user_message})
    
    try:
        # definindo as características do chatbot
        response = client.chat.completions.create(
            model = "gemma-3-4b-it-qat",
            messages = chat_history,
            temperature = 0.7,
        )
    
        # retornando requisições HTTP da API do LM Studio
        reply = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"erro ": str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(debug=True)

