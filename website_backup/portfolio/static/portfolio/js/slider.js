const slides = document.querySelector('.slides');
const slideCount = document.querySelectorAll('.slide').length;
let currentIndex = 0;

function showNextSlide() {
  currentIndex++;
  if (currentIndex >= slideCount / 2) { // Поскольку у нас есть дублированные слайды
    currentIndex = 0;
    slides.style.transition = 'none';
    slides.style.transform = `translateX(0)`;
    setTimeout(() => {
      slides.style.transition = 'transform 1s ease';
      showNextSlide();
    }, 20);
  } else {
    slides.style.transform = `translateX(-${currentIndex * 20}%)`;
  }
}

setInterval(showNextSlide, 3000); // Смена слайдов каждые 3 секунды
