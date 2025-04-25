async function sendMessage() {
    // instanciando os objetos de inout e chat
    const userInput = document.getElementById("user-input");
    const userMessage = userInput.value;

    if(!userMessage){
      return;
    }

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class='user'><strong>Você:</strong> ${userMessage}</div>`;
    userInput.value = "";

    // fazendo a conexão com a API do backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
      });

    const data = await response.json();
    chatBox.innerHTML += `<div class='bot'><strong>FURIAbot:</strong> ${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

}