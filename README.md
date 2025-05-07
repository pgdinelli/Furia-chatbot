# Furia-chatbot
Aplicação web de um chatbot que conversa com fãs do time de CS da Furia e passa informações sobre jogadores, campeonatos e produtos da loja do time.
## Sobre a aplicação
A aplicação trata-se de uma IA que utiliza o modelo "gemma-3" da Google, mas que foi treinada para agir como um super fã da organização de esportes eletrônicos "Furia", utilizando de prompts inseridos diretamente no código. O chatbot conversa com outros fãs do time e utiliza de emotes e gírias animadas para que a interação seja dinâmica e menos robotizada. 
### Como funciona
Para utilização do modelo gemma 3 foi usado um software chamado "LM Studio" que permite rodar uma LLM (Large Language Model) localmente na sua própria máquina, você escolhe entre uma variedade de modelos que o software oferece e baixa para o computador ou servidor onde a LLM irá rodar. Além disso, o LM Studio possui compatibilidade com API da OpenAI tornando o software uma alternativa grátis para se trabalhar com LLMs e fazer requisições HTTP que retornam a resposta do chatbot para o frontend. O sistema foi desenvolvido com linguagem de programação Python e o framework Flask foi utilizado para conexão com aplicação web no seu backend. Já a parte do frontend foi feita com HTML, CSS e JavaScript puros para manter a janela de chat simples, porém totalmente funcional. 
## Aplicação em funcionamento
### 1 - Tela inicial da aplicação, janela de chat vazia assim que acessa o sistema
![Frontend-telaInicial](https://github.com/user-attachments/assets/10c3eca4-eb10-4d33-872c-28c23e87c49c)
### 2 - Conversa em tempo real com o bot da Furia
![Frontend-ConversaFuncional](https://github.com/user-attachments/assets/63aab382-a216-47ac-9db4-10ca416c52b9)
### 3 - Chatbot passando informações recentes do time
![Chatbot-Informacoes](https://github.com/user-attachments/assets/0b46d27f-21d0-48a6-8743-027dd4f8bf26)
### 4 - Log do LM Studio com respostas das requisições em formato Json
![LMStudio-RequisicoesJson](https://github.com/user-attachments/assets/cd6e6b3e-e04a-46f5-bfb8-9e07595bb33d)


O bot conta com uma memória de conversa implementada em seu backend, desta forma o bot guarda informações ditas pelo usuário durante toda a conversa, como pode ser visto entre a imagem 2 onde é iniciada uma conversa com o usuário apresentando seu nome e na imagem 3, ao agradecer pela informação passada, o bot responde se referindo ao usuário pelo mesmo nome que foi dito anteriormente.

# Frontend
Deploy feito na Vercel. 
- Pode ser acessado através do link: https://furia-chatbot-wheat.vercel.app
### Tecnologias utilizadas
- HTML
- CSS
- JavaScript
### Código fonte
https://github.com/pgdinelli/Furia-chatbot/tree/main/frontend
# Backend
Até o presente momento a única forma de rodar o backend é em uma máquina local, devido ao uso do LM Studio que não permite conexão de origens diferentes através da web. 

### Algumas soluções para resolver este problema:
- Utilizar a API original da OpenAI sem compatibilidade com a API do LM Studio, porém é um serviço pago.
- Rodar o modelo de LLM em uma aplicação em nuvem, que seria uma implementação complexa.
- Baixar o LM Studio em sua própria máquina e rodar o modelo localmente.

Por conta desta limitação, ao acessar o chat pela Vercel será possível enviar mensagens normalmente já que esta funcionalidade é feita pela parte do frontend, porém o usuário não receberá resposta nenhuma.
### Como eu resolvi este problema parcialmente:
Utilizando uma ferramenta chamada ngrok é possível criar uma espécie de "túnel" entre um servidor rodando localmente e uma máquina externa, desta forma outras pessoas podem conversar e receber respostas do bot normalmente para fins de demonstração do projeto. Isto só irá funcionar enquanto o servidor estiver rodando na máquina local, no momento que o ngrok for encerrado ele irá fechar o "túnel" e não será mais possível que outras máquinas possam receber respostas do bot.
### Tecnologias utilizadas
- Python
- Flask
- API OpenAI
- LM Studio
- ngrok
### Código fonte
https://github.com/pgdinelli/Furia-chatbot/tree/main/backend
# Referências
- Documentação Flask: https://flask.palletsprojects.com/en/stable/
- Documentação LM Studio: https://lmstudio.ai/docs/app
- Documentação OpenAI API: https://platform.openai.com/docs/overview
- Documentação ngrok: https://ngrok.com/docs
# Autor
Paulo Guilherme Souza Dinelli.<br>
Linkedin: https://www.linkedin.com/in/paulodinelli
