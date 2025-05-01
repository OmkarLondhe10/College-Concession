/*document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Process contact form (e.g., send an email or save to a database)
            alert(`Contact form submitted by ${name} with email ${email}. Message: ${message}`);
        });
    }
});*/

// About.html
document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');
  
    menuToggle.addEventListener('click', function () {
      nav.classList.toggle('active');
    });
  });
  
  document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('.gallery-slide');
    const totalSlides = slides.length;
    let currentIndex = 0;

    function showNextSlide() {
      slides.forEach((slide, index) => {
        slide.style.transform = `translateX(-${100 * currentIndex}%)`;
      });

      currentIndex = (currentIndex + 1) % totalSlides; // Loop back to the start
    }

    // Set the interval to change slides every 3 seconds
    setInterval(showNextSlide, 3000);
  });  

// Initialize SwiperJS
var swiper = new Swiper('.swiper-container', {
  slidesPerView: 1, // Show one slide at a time
  spaceBetween: 10,
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },
  loop: true, // Infinite loop for slides
});
