
const passwordField = document.querySelector('.password-field');
const toggleButton = document.querySelector('.toggle-password');

toggleButton.addEventListener('click', function() {
  if (passwordField.type === 'password') {
    passwordField.type = 'text';
    toggleButton.querySelector('i').classList.remove('fa-eye');
    toggleButton.querySelector('i').classList.add('fa-eye-slash');
  } else {
    passwordField.type = 'password';
    toggleButton.querySelector('i').classList.remove('fa-eye-slash');
    toggleButton.querySelector('i').classList.add('fa-eye');
  }
});

