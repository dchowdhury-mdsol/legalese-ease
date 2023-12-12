const messageBar = document.getElementById("messageBar");
const sendBtn = document.getElementById("sendBtn");
const chatHistory = document.getElementById("chatHistory");

function sendMessage() {
    if (messageBar.value.trim()) {
        let message = `<div class="message">${messageBar.value}</div>`;
        chatHistory.innerHTML += message;
        messageBar.value = '';
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
}

messageBar.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});

sendBtn.addEventListener('click', sendMessage);