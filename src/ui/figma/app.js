const messageBar = document.querySelector(".bar-wrapper input");
const sendBtn = document.querySelector(".bar-wrapper button");
const messageBox = document.querySelector(".message-box");

function sendMessage() {
    if (messageBar.value.length > 0) {
        let message = `<div class="chat message">
            <span class="material-symbols-outlined">
                person
            </span>
            <span>
                ${messageBar.value}
            </span>
        </div>`;
        
        messageBox.insertAdjacentHTML("beforeend", message);
        messageBar.value = '';
    }
}

messageBar.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

sendBtn.onclick = sendMessage;
