document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const themeToggle = document.querySelector('.theme-toggle');
    const spinner = document.querySelector('.loading-spinner');

    // Apply fade-in effect
    body.classList.add('fade-in');

    // Theme toggle functionality
    const themeToggleButton = document.querySelector(".theme-toggle");
    const moonIcon = document.createElement("span");
    moonIcon.classList.add("moon");
    moonIcon.textContent = "🌙"; // Moon for dark mode
    const sunIcon = document.createElement("span");
    sunIcon.classList.add("sun");
    sunIcon.textContent = "🌞"; // Sun for light mode

// Append both icons to the button
    themeToggle.appendChild(moonIcon);
    themeToggle.appendChild(sunIcon);

// Set initial mode based on localStorage
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
        sunIcon.style.display = "none"; // Hide sun
        moonIcon.style.display = "inline-block"; // Show moon
    } else {
        document.body.classList.add("light-mode");
        moonIcon.style.display = "none"; // Hide moon
        sunIcon.style.display = "inline-block"; // Show sun
    }

// Toggle dark/light mode
    themeToggle.addEventListener("click", () => {
        const isDarkMode = document.body.classList.toggle("dark-mode");
        document.body.classList.toggle("light-mode", !isDarkMode);

        if (isDarkMode) {
            localStorage.setItem("darkMode", "true");
            sunIcon.style.display = "none"; // Hide sun
            moonIcon.style.display = "inline-block"; // Show moon
        } else {
            localStorage.setItem("darkMode", "false");
            moonIcon.style.display = "none"; // Hide moon
            sunIcon.style.display = "inline-block"; // Show sun
        }
    });

    document.addEventListener('DOMContentLoaded', function () {
        document.body.classList.add('fade-in');
        const links = document.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', function (event) {
                event.preventDefault();
                document.body.classList.remove('fade-in');
                setTimeout(() => {
                    window.location.href = this.href;
                }, 500);
            });
        });
    });
});


