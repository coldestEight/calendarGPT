chat = document.getElementById('chat')
linebreak = document.createElement("br")
userIn = document.getElementById("userTextIn")
sendButton = document.getElementById("sendButton")
generatingMsg = document.getElementById("generatingMsg")

sendButton.onclick = sendUserChat

isGenerating = false


//Checks if a request is active to stop user from sending more inputs
$(document).ajaxStart(function(){

    isGenerating = true
    generatingMsg.style.display = "block"

}).ajaxStop(function(){

    isGenerating = false
    generatingMsg.style.display = "none"

})

//get initial AI response when the page loads via POST request
$(document).ready(function() {
    
    $.ajax({
        type: 'POST',
        url: '/run_init',
        success: function(response) {

            gptChat = document.createElement("p");
            gptChat.innerHTML = response.response;
            gptChat.classList.add("gptChat")
            chat.append(linebreak.cloneNode())
            chat.append(gptChat)
        },
        error: function(error) {
            console.error('Error:', error);
        }
    })
})


//get user response from textbox and send to AI via POST request
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
                gptChat.innerHTML = response.response
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

//call sendUserChat when the enter key is pressed while clicked onto textbox
userIn.addEventListener('keydown',function(){
    if(event.key == "Enter"){

        sendUserChat()
    }
});
