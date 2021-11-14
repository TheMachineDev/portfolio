var menu = document.getElementById("menu");
var hamburger = document.getElementById("hamburger");
hamburger.addEventListener("click", () => {
  if (menu.classList.contains('toggled')) {
    menu.classList.remove('toggled')
    document.body.style.overflow = 'visible'
  }
  else {
    menu.classList.add('toggled')
    document.body.style.overflow = 'hidden'
  }
});


let resizeTimer;
window.addEventListener("resize", () => {
  document.body.classList.add("resize-animation-stopper");
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    document.body.classList.remove("resize-animation-stopper");
  }, 100);
});