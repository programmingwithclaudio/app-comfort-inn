const toggleTheme = () => {
    const body = document.querySelector('body');
    body.classList.toggle('dark-theme');
};

const darkModeButton = document.querySelector('.dark-mode');
darkModeButton.addEventListener('click', toggleTheme);