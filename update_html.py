import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_tag = '<section class="cake-section" id="cakeSection">'
end_tag = '</section>'

start_idx = html.find(start_tag)
end_idx = html.find(end_tag, start_idx) + len(end_tag)

new_content = """
  <!-- Act 5: Shinchan Interactive Slide Game -->
  <section class="cake-section" id="cakeSection">
    <div id="slideGameContainer">
      <!-- Slide 1 -->
      <div class="slide slide-1 active" id="slide-1">
        <h2>Are you really excited?</h2>
        <img src="media/shinchan-excited.gif" alt="Shinchan Excited" class="shinchan-img" onerror="this.src='https://placehold.co/400x300/ffdddd/ff0000?text=Shinchan+Excited'">
        <div class="btn-group">
          <button class="game-btn yes-btn" onclick="goToSlide(2)">YES</button>
          <button class="game-btn yes-btn" onclick="goToSlide(2)">YES</button>
        </div>
      </div>

      <!-- Slide 2 -->
      <div class="slide slide-2" id="slide-2">
        <h2>I have made something for you<br>Do you wanna see it?</h2>
        <img src="media/shinchan-happy.gif" alt="Shinchan Happy" class="shinchan-img" onerror="this.src='https://placehold.co/400x300/ffdddd/ff0000?text=Shinchan+Happy'">
        <div class="btn-group">
          <button class="game-btn yes-btn" onclick="goToSlide(4)">YES</button>
          <button class="game-btn no-btn" onclick="goToSlide(3)">NO</button>
        </div>
      </div>

      <!-- Slide 3 (NO Path) -->
      <div class="slide slide-3" id="slide-3">
        <h2>HOW DARE YOU!</h2>
        <img src="media/shinchan-angry.gif" alt="Shinchan Angry" class="shinchan-img" onerror="this.src='https://placehold.co/400x300/ffdddd/ff0000?text=Shinchan+Angry'">
        <button class="game-btn try-again-btn" onclick="goToSlide(2)">TRY AGAIN</button>
      </div>

      <!-- Slide 4 (Gifts) -->
      <div class="slide slide-4" id="slide-4">
        <h2>Each gift has something for you...<br>CLICK ON THE GIFTS</h2>
        <div class="gifts-container">
          <img src="media/gift-box.png" alt="Gift 1" class="gift-box" onclick="goToSlide(5)" onerror="this.src='https://placehold.co/150x150/ff4d4d/fff?text=Gift'">
          <img src="media/gift-box.png" alt="Gift 2" class="gift-box" onclick="goToSlide(6)" onerror="this.src='https://placehold.co/150x150/ff4d4d/fff?text=Gift'">
          <img src="media/gift-box.png" alt="Gift 3" class="gift-box" onclick="goToSlide(7)" onerror="this.src='https://placehold.co/150x150/ff4d4d/fff?text=Gift'">
        </div>
      </div>

      <!-- Slide 5 (Gift 1) -->
      <div class="slide slide-5 gift-slide" id="slide-5">
        <button class="back-btn" onclick="goToSlide(4)">← Back</button>
        <div class="card-layout">
          <div class="card-text">
            <h1>Happy Birthday</h1>
            <p>Wishing you a little bit of happiness, love, laughter, and joy today & always.</p>
            <h3>Chinni Nana</h3>
          </div>
          <div class="card-photo">
            <img src="media/photo1.jpg" alt="Photo" onerror="this.src='https://placehold.co/200x250/ccc/fff?text=Your+Photo'">
          </div>
        </div>
      </div>

      <!-- Slide 6 (Gift 2) -->
      <div class="slide slide-6 gift-slide" id="slide-6">
        <button class="back-btn" onclick="goToSlide(4)">← Back</button>
        <h1>MAKE A WISH</h1>
        <p class="love-text">i love you</p>
        <img src="media/cake-graphic.png" alt="Cake Graphic" class="cake-img" onerror="this.src='https://placehold.co/400x300/ffebcd/ff0000?text=Cake+Graphic'">
      </div>

      <!-- Slide 7 (Gift 3) -->
      <div class="slide slide-7 gift-slide" id="slide-7">
        <button class="back-btn" onclick="goToSlide(4)">← Back</button>
        <h1 class="memories-title">MEMORIES</h1>
        <div class="polaroid-container">
          <div class="polaroid"><img src="media/photo2.jpg" alt="Memory" onerror="this.src='https://placehold.co/150x150/ccc/fff?text=Photo'"><div class="caption">❤️</div></div>
          <div class="polaroid"><img src="media/photo3.jpg" alt="Memory" onerror="this.src='https://placehold.co/150x150/ccc/fff?text=Photo'"><div class="caption">✨</div></div>
          <div class="polaroid"><img src="media/photo4.jpg" alt="Memory" onerror="this.src='https://placehold.co/150x150/ccc/fff?text=Photo'"><div class="caption">🥰</div></div>
        </div>
        <button class="game-btn next-btn" onclick="goToSlide(8)">Read Letter →</button>
      </div>

      <!-- Slide 8 (Letter) -->
      <div class="slide slide-8" id="slide-8">
        <h2 class="fav-person">My fav person</h2>
        <div class="letter-content">
          <p>Dear bestie,<br>Happy Birthday, Chinni Nana! ❤️</p>
          <p>I honestly don't know how to put into words how grateful I am to have you in my life. Thank you for being my biggest supporter, my partner in crime, and the person I can always count on. Through all the laughs, random conversations, inside jokes, and even the tough days, you've made life so much better just by being a part of it.</p>
          <p>I hope this year brings you everything you've been wishing for—happiness, success, peace, good health, and countless reasons to smile. Never forget how amazing, kind, and loved you are. You deserve nothing but the very best.</p>
          <p>No matter where life takes us, I hope we always stay this close and keep making memories together. Thank you for being the wonderful person you are and for making my life brighter every single day.</p>
          <p>Have the happiest birthday, and enjoy every moment of your special day. I love you so much!</p>
          <p>Love you 💕</p>
        </div>
        <button class="game-btn next-btn" onclick="goToSlide(9)">Next →</button>
      </div>

      <!-- Slide 9 (Ending) -->
      <div class="slide slide-9" id="slide-9">
        <h2>May all the good things you've been waiting for finally find you this year ❤️</h2>
        <img src="media/shinchan-cute.gif" alt="Shinchan Cute" class="shinchan-img" onerror="this.src='https://placehold.co/400x300/ffdddd/ff0000?text=Shinchan+Cute'">
      </div>
    </div>
  </section>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html[:start_idx] + new_content + html[end_idx:])
