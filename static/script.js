function startApp() {
    const welcomeSection = document.getElementById('welcome-section');
    const optionsSection = document.getElementById('options');

    welcomeSection.classList.add('fade-out');

    setTimeout(() => {
        welcomeSection.style.display = 'none';
        optionsSection.classList.add('show-options');
    }, 800);
}
