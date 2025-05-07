// instanciando os objetos de input botão de enviar mensagem
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

// Enviar mensagem com a tecla "ENTER"
userInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
});

async function sendMessage() {

  const userMessage = userInput.value.trim();

  if (!userMessage) {
    return;
  }

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += ` <div class="message user">
      <div class="sender">Você:</div>
      <div class="text">${userMessage}</div>
    </div>`;
  userInput.value = "";


  // fazendo a conexão com a API do backend, utilizando túnel do ngrok para uso do chatbot por terceiros
  const response = await fetch("https://b221-2804-d4b-c511-4800-a048-5d38-248-ebdb.ngrok-free.app/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await response.json();
  chatBox.innerHTML += `
  <div class='message bot'>
    <div class='sender'>Pantera Negra:</div>
    <div class="bot-content">
      <img src="Furia_Esports_logo.png" alt="Logo da Furia" class="bot-logo">
      <div class="text">${data.reply}</div>
    </div>
  </div>`;
  chatBox.scrollTop = chatBox.scrollHeight;

}