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
    "Se perguntado sobre a posição da Furia no rank mundial atual, diga que está no top 17 do mundo."
    "Se perguntado sobre o próximo jogo da Furia, diga que é contra o time da The Mongolz, dia 10 de maio de 2025 no campeonato da PGL Astana 2025."
    "Se perguntando quais os próximos campeonatos da Furia, diga que já está confirmada para jogar a PGL Astana 2025 que começa dia 10 de maio, a IEM Dallas 2025 que começa dia 19 de maio e BLAST Austin Major 2025 dia 7 de junho."
    "Se não tiver informações dos próximos jogos ou campeonatos da Furia, diga que demais informações podem ser conferidas no site hltv.org."
    "Se perguntado onde comprar produtos da Furia, diga que pode conferir no site https://www.furia.gg e que tem camisas, boné, moletons, mochilas e tudo para um fã da Furia usar."
)

# instanciando uma aplicação em Flask
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': 'https://furia-chatbot-wheat.vercel.app'}})

# Armazenando histórico de conversa na memória
chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

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

