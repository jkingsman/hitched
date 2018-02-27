function authreq(endpoint, method, data, onError, onSuccess) {
  var formData = new FormData();
  if (data) {
    for (const key in data) {
      console.log(key)
      formData.append(key, data[key]);
    }
  }

  var xhr = new XMLHttpRequest();

  if (document.cookie.split('sessionToken=').len > 1) {
    // we have a session
    xhr.setRequestHeader('Authorization', 'Token ' +
      document.cookie.split('sessionToken=')[1]);
  }

  xhr.open(method, endpoint, true);
  xhr.onload = function(e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        if (typeof onSuccess === "function") {
          response = JSON.parse(xhr.responseText);
          onError(response);
        }
      } else {
        if (typeof onSuccess === "function") {
          response = JSON.parse(xhr.responseText);
          onError(response, xhr);
        }
        console.error(xhr);
      }
    }
  };

  xhr.onerror = function(e, xhr) {
    document.getElementById('badPassword').classList.remove('hidden');
    setTimeout(() => (document.getElementById('badPassword').classList.remove('hidden')), 4000);
  };

  xhr.send(formData);
}

if (document.cookie.split('sessionToken=').length > 1 &&
  (window.location.pathname == '/index.html' ||
    window.location.pathname == '/') && window.location.hash !== "#logout") {
      console.log(window.location.hash)
  window.location = '/admin.html';
} else if (document.cookie.split('sessionToken=').length < 2 &&
  window.location.pathname == '/admin.html') {
  window.location = '/index.html';
}
