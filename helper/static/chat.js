document.getElementById('send-btn').addEventListener('click', function() {
    var userInput = document.getElementById('user-input');
    var message = userInput.value;
    userInput.value = '';  


    var chatBox = document.getElementById('chat-box');
    var userDiv = document.createElement('div');
    userDiv.textContent = message;
    userDiv.className = 'message user-message'; 
    chatBox.appendChild(userDiv);

    fetch('/chat/', {
        method: 'POST',
        body: JSON.stringify({message: message}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') 
        }
    })
    .then(response => response.json())
    .then(data => {

                var botDiv = document.createElement('div');
                botDiv.style.whiteSpace= 'pre-line';
                botDiv.textContent = data.bot_message;
                botDiv.className = 'message bot-message'; 
                chatBox.appendChild(botDiv);
                chatBox.appendChild(document.createElement('br'))
                chatBox.scrollTop = chatBox.scrollHeight;
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var input = document.getElementById("user-input");

input.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Cancel the default action, if needed
      event.preventDefault();
      // Trigger the button element with a click
      document.getElementById("send-btn").click();
    }
  });