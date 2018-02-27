document.addEventListener("DOMContentLoaded", function(event) {
  document.getElementById('loginTrigger').addEventListener('click', handleForm);
  document.getElementById('loginForm').addEventListener('submit', handleForm);
});


function handleForm(event) {
  event.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  var formData = new FormData();

  formData.append("username", username);
  formData.append("password", password);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "http://127.0.0.1:8000/get-token/", true);
  xhr.onload = function(e) {
    console.log(xhr)
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        token = JSON.parse(xhr.responseText).token;
        document.cookie = "sessionToken=" + token;
        document.location = "/admin.html";
      } else {
        console.error(xhr.statusText);
      }
    }
  };

  xhr.onerror = function(e, xhr) {
    document.getElementById('badPassword').classList.remove('hidden');
    setTimeout(() => (document.getElementById('badPassword').classList.add('hidden')), 4000);
  };

  xhr.send(formData);
}

if (window.location.hash == "#logout") {
  authreq('http://127.0.0.1/discard-token/', 'GET', null, null);
  document.cookie = 'sessionToken=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  document.getElementById('loggedOut').classList.remove('hidden');
  setTimeout(function() {
    document.getElementById('loggedOut').classList.add('hidden');
    window.location.hash = '';
  }, 4000);
}
