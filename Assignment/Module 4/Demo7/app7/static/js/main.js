// static/js/main.js
document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll('input');

    inputs.forEach(input => {
        // Add a subtle scale effect to the parent container when focused
        input.addEventListener('focus', () => {
            input.parentElement.style.transform = 'scale(1.02)';
            input.parentElement.style.transition = 'transform 0.3s ease';
        });

        input.addEventListener('blur', () => {
            input.parentElement.style.transform = 'scale(1)';
        });
    });
});