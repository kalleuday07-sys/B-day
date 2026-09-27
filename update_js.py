import re

with open('birthday.js', 'r', encoding='utf-8') as f:
    js = f.read()

start_idx = js.find("/* ============================================================\n   CAKE SECTION OBSERVER & MIC LOGIC")

new_js = """/* ============================================================
   SHINCHAN GAME LOGIC
   ============================================================ */
const cakeSection = document.getElementById('cakeSection');

// Expose slide navigation globally
window.goToSlide = function(slideNumber) {
  // Hide all slides
  const slides = document.querySelectorAll('.slide');
  slides.forEach(s => s.classList.remove('active'));
  
  // Show target slide
  const target = document.getElementById('slide-' + slideNumber);
  if (target) {
    target.classList.add('active');
  }
};

if (cakeSection) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        cakeSection.classList.add('is-active');
      }
    });
  }, { threshold: 0.3 });
  observer.observe(cakeSection);
}
"""

with open('birthday.js', 'w', encoding='utf-8') as f:
    f.write(js[:start_idx] + new_js)
