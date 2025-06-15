document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM fully loaded");

    // Handle Signup Form Submission
    const signupForm = document.getElementById('signup-form');
    if (signupForm) {
        console.log("Signup form found!");

        signupForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent default form submission

            // Get form values
            const name = document.getElementById('signup-name').value.trim();
            const email = document.getElementById('signup-email').value.trim();
            const password = document.getElementById('signup-password').value;
            const confirmPassword = document.getElementById('signup-confirm-password').value;

            // Validate password match
            if (password !== confirmPassword) {
                alert("Passwords do not match!");
                return;
            }

            // Retrieve CSRF token from the form
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            try {
                const response = await fetch('/signup/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({ name, email, password })
                });

                const data = await response.json();
                if (response.ok) {
                    alert('Signup successful! Redirecting to login page...');
                    window.location.href = 'login.html';  // Redirect to login page
                } else {
                    alert(data.error || 'Signup failed! Please try again.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            }
        });
    }
});



//login
document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM fully loaded");

    // Handle Login Form Submission
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        console.log("Login form found!");

        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent default form submission

            // Get form values
            const email = document.getElementById('login-email').value.trim();
            const password = document.getElementById('login-password').value;

            // Check if email and password are not empty
            if (!email || !password) {
                alert('Please enter both email and password.');
                return;
            }

            // Retrieve CSRF token from the form
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            try {
                const response = await fetch('/login/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                if (response.ok) {
                    alert('Login successful! Redirecting to main page...');
                    window.location.replace('main.html');  // Redirect to main.html
                } else {
                    alert(data.error || 'Invalid email or password!');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            }
        });
    }
});

// Function to toggle password visibility
function togglePasswordVisibility(inputId, button) {
    const input = document.getElementById(inputId);
    if (input.type === 'password') {
        input.type = 'text';
        button.textContent = '🙈';
    } else {
        input.type = 'password';
        button.textContent = '👁️';
    }
}


// Function to toggle password visibility
function togglePasswordVisibility(inputId, button) {
    const input = document.getElementById(inputId);
    if (input.type === 'password') {
        input.type = 'text';
        button.textContent = '🙈';
    } else {
        input.type = 'password';
        button.textContent = '👁️';
    }
}
