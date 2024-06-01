const toggleMenu = () => {
    const navigation = document.querySelector('.navigation');
    const burgerMenu = document.querySelector(".menu-icon");
    const src = burgerMenu.getAttribute('src');
    const isBurger = src === './static/imgs/burger-menu.svg';
    const iconName = isBurger ? './static/imgs/close.svg' : './static/imgs/burger-menu.svg';
    burgerMenu.setAttribute('src', iconName);

    if (!isBurger) {
        navigation.classList.add("navigation--mobile--fadeout");
        setTimeout(() => {
            navigation.classList.remove('show'); // Ocultar el menú al hacer clic en el ícono del menú
            navigation.classList.toggle('navigation--mobile');
        }, 300);
    } else {
        navigation.classList.remove("navigation--mobile--fadeout");
        navigation.classList.add('show'); // Mostrar el menú al hacer clic en el ícono del menú
        navigation.classList.toggle('navigation--mobile');
    }
};

