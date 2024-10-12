const hb = document.querySelector(".header__hamburger");
const menu = document.querySelector(".header");
const body = document.querySelector("body");
const menuLinks = document.querySelectorAll(".header__menu a");

hb.addEventListener("click", function () {
  menu.classList.toggle("active");
  body.classList.toggle("lock");
});

menuLinks.forEach(link => {
  link.addEventListener("click", function() {
    menu.classList.remove("active");
    body.classList.remove("lock");
  });
});