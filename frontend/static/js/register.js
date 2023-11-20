document.getElementById('register-form').addEventListener('submit', function(e) {
    e.preventDefault();

    var username = document.getElementById('register-username').value;
    var email = document.getElementById('register-email').value;
    var password = document.getElementById('register-password').value;

    fetch('/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            // Display message
            document.getElementById('register-error-message').textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
