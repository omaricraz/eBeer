// V2-Scripts: carousel.js

document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.carousel-container');
  const items = document.querySelectorAll('.carousel-item');
  const prevBtn = document.querySelector('.carousel-prev');
  const nextBtn = document.querySelector('.carousel-next');
  let index = 0;

  function updateCarousel() {
    container.style.transform = `translateX(-${index * 100}%)`;
  }

  prevBtn.addEventListener('click', () => {
    index = (index === 0) ? items.length - 1 : index - 1;
    updateCarousel();
  });

  nextBtn.addEventListener('click', () => {
    index = (index === items.length - 1) ? 0 : index + 1;
    updateCarousel();
  });

  // Optional: auto-play every 5 seconds
  setInterval(() => {
    nextBtn.click();
  }, 5000);
});
