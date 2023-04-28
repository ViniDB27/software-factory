let menuOpen = false;

const menu = document.querySelector('.mobile-nav-wrapper');
const submenu = document.querySelector('.nav-bar-mobile-items-container');

const menuButton = document.querySelector('.menu-btn');

menuButton.addEventListener('click', (element) => {
    if (!menuOpen) {
        menu.classList.add('mobile-nav-wrapper-open');
        submenu.style.display = 'flex';
        menuOpen = true;
    } else {
        menu.classList.remove('mobile-nav-wrapper-open');
        submenu.style.display = 'none'
        menuOpen = false;
    }
})