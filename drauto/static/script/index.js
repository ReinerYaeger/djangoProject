let menu = document.querySelector('#menu-icon');
let navabr = document.querySelector('.navbar');

menu.onClcik = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('open');
}