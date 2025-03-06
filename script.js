const wrapper = document.querySelector('.wrapper');
    
function registerActive() {
    wrapper.classList.toggle('active');
}

function loginActive() {
    wrapper.classList.toggle('active');
}

// Handle registration form submission
document.getElementById('register-form').onsubmit = function(event) {
    event.preventDefault();

    const fullName = document.getElementById('full-name').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;

    fetch('http://127.0.0.1:8000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            full_name: fullName,
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('register-message').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('register-message').textContent = 'Error: ' + error.message;
    });
};

// Handle login form submission
document.getElementById('login-form').onsubmit = function(event) {
    event.preventDefault();

    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(response => {
        if (response.ok) {
            // Use JavaScript to redirect to c.html
            window.location.href = "c.html";  // Redirect to c.html
        } else {
            response.json().then(data => {
                document.getElementById('login-message').textContent = data.message;
            });
        }
    })
    .catch(error => {
        document.getElementById('login-message').textContent = 'Error: ' + error.message;
    });
}