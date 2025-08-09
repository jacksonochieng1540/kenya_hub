// ===== Kenya Tech Hub Main JavaScript =====

// Show confirmation before attending an event
document.addEventListener('DOMContentLoaded', function () {
    const attendButtons = document.querySelectorAll('.attend-btn');
    attendButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            if (!confirm("Are you sure you want to attend this event?")) {
                e.preventDefault();
            }
        });
    });
});

// Auto-hide Bootstrap alerts after 5 seconds
setTimeout(function () {
    let alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        let fadeEffect = setInterval(function () {
            if (!alert.style.opacity) {
                alert.style.opacity = 1;
            }
            if (alert.style.opacity > 0) {
                alert.style.opacity -= 0.05;
            } else {
                clearInterval(fadeEffect);
                alert.remove();
            }
        }, 50);
    });
}, 5000);

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Toggle dark mode (future feature)
document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function () {
            document.body.classList.toggle('dark-mode');
            localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
        });

        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('dark-mode');
        }
    }
});
// Auto-hide alerts after 5 seconds
setTimeout(function () {
    let alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        let fadeEffect = setInterval(function () {
            if (!alert.style.opacity) {
                alert.style.opacity = 1;
            }
            if (alert.style.opacity > 0) {
                alert.style.opacity -= 0.05;
            } else {
                clearInterval(fadeEffect);
                alert.remove();
            }
        }, 50);
    });
}, 5000);
