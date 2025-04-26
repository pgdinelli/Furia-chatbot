// instanciando os objetos de input e chat
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

  const userMessage = userInput.value;

  if (!userMessage) {
    return;
  }

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class='user'><strong>Você:</strong> ${userMessage}</div>`;
  userInput.value = "";


  // fazendo a conexão com a API do backend
  const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await response.json();
  chatBox.innerHTML += `<div class='bot'><strong>FURIAbot:</strong> ${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;

}