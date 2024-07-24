btn = document.getElementById("btn");
var fname = document.getElementById("fname");
var email = document.getElementById("email");
var num = document.getElementById("num");

var fullname = fname.value;
var mail = email.value;
var number = num.value;


form.addEventListener('submit', (event) => {
        window.location.href="index.html";
        event.preventDefault();
        alert("You are logged in!!");
});

