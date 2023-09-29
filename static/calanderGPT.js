chat = document.getElementById('chat')
linebreak = document.createElement("br")
userIn = document.getElementById("userTextIn")
sendButton = document.getElementById("sendButton")

sendButton.onclick = sendUserChat

isGenerating = false

userIn.addEventListener('keydown',function(){
    if(event.key == "Enter"){

        sendUserChat()
    }
});


$(document).ready(function() {
    // Send a POST request to the /run_function route when the page loads
    
    $.ajax({
        type: 'POST',
        url: '/run_init',
        success: function(response) {

            gptChat = document.createElement("p");
            gptChat.textContent = response.response;
            gptChat.classList.add("gptChat")
            chat.append(linebreak.cloneNode())
            chat.append(gptChat)
        },
        error: function(error) {
            console.error('Error:', error);
        }
    })
})

$(document).ajaxStart(function(){

    isGenerating = true

}).ajaxStop(function(){

    isGenerating = false

})


function sendUserChat(){
    userText = userIn.value

    if(userText != "" && !isGenerating){

        userChat = document.createElement("p")
        userChat.textContent = userText
        userChat.classList.add("userChat")
        chat.append(linebreak.cloneNode())
        chat.append(userChat)

        userIn.value = ""

        userInJSON = {"userIn": userText}

        $.ajax({
            type: 'POST',
            data: JSON.stringify(userInJSON),
            url: '/get_message',
            contentType:'application/json',
            success: function(response) {

                gptChat = document.createElement("p")
                gptChat.textContent = response.response
                gptChat.classList.add("gptChat")
                chat.append(linebreak.cloneNode())
                chat.append(gptChat)
            },
            error: function(error) {
                console.error('Error:', error)
            }
        });

    }
}

