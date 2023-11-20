document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();

    var username = document.getElementById('login-username').value;
    var password = document.getElementById('login-password').value;

    fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Handle successful login (e.g., redirect to dashboard)
        } else {
            // Display error message
            document.getElementById('login-error-message').textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
