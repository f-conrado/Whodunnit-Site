function openForm() {
  document.getElementById("myModal").style.display = "block";
}

function closeForm() {
  document.getElementById("myModal").style.display = "none";
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function gfg_Run() {
    var textarea = document.getElementById('bottom');
    textarea.scrollTop = textarea.scrollHeight;
       }

var csrf = document.getElementsByName('csrfmiddlewaretoken');

$(document).ready(function(){

    //var csrf = document.getElementsByName('csrfmiddlewaretoken');


});

//console.log("1");




/*function sending() {
    let chatBody = document.getElementById("campo");
    let messageSend = document.getElementById("input");
    let a = $("#input").val();
    console.log(messageSend);
    chatBody.innerHTML = a;
}*/

function entere(){
    var supere = document.getElementById('input');
    supere.addEventListener("keydown", yes, true);
};

function focus() {
    var supere = document.getElementById('input');
    supere.focus();
};

function yes(){
    var supere = document.getElementById('input');
    supere.removeEventListener("keydown", yes);
    if(event.keyCode == "13") {
            sending();
        };
};

function sending() {
    $.ajax({
            url: 'send/',
            type: 'GET',
            data: {
                input_text: $("#input").val()
                //CSRF: csrf
            },
            success: function(response){
                let userSpeak = '<p class="mensagem usador"><span>' + response.data + '</span></p>'
                var textarea = document.getElementById('campo');
                $("#input").val("");
                if (!(response.data == '')) {
                    $("#campo").append(userSpeak);
                    textarea.scrollTop = textarea.scrollHeight
                    let botSpeak = '<p class="mensagem"><span>' + response.b + '</span></p>'
                    setTimeout(function() { $("#campo").append(botSpeak),
                    textarea.scrollTop = textarea.scrollHeight }, 2000);
                };

            }
        });
}