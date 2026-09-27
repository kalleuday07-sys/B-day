import re

with open('birthday.css', 'r', encoding='utf-8') as f:
    css = f.read()

start_tag = '.cake-section {'
end_tag = '/* Scroll indicator */'

start_idx = css.find(start_tag)
end_idx = css.find(end_tag)

new_css = """
/* ============================================================
   SHINCHAN GAME CSS
   ============================================================ */
.cake-section {
  position: relative;
  width: 100%;
  height: 100vh;
  background: #fdf6e3;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
}
#slideGameContainer {
  position: relative;
  width: 90vw;
  max-width: 800px;
  height: 80vh;
  background-color: #fff;
  border: 15px solid #d4235c;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  overflow: hidden;
  opacity: 0;
  transition: opacity 1.5s ease;
}
.cake-section.is-active #slideGameContainer {
  opacity: 1;
}

.slide {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  padding: 2em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.5s ease, transform 0.5s ease;
  transform: translateX(50px);
}
.slide.active {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(0);
}

.slide h2, .slide h1 {
  color: #d4235c;
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.shinchan-img, .cake-img {
  max-width: 60%;
  max-height: 40vh;
  border-radius: 10px;
  margin-bottom: 20px;
}

.btn-group {
  display: flex;
  gap: 20px;
}

.game-btn {
  padding: 15px 40px;
  font-size: 1.5rem;
  font-weight: bold;
  border-radius: 30px;
  border: none;
  cursor: pointer;
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
  transition: transform 0.2s;
  font-family: inherit;
}
.game-btn:active {
  transform: scale(0.95);
}
.yes-btn {
  background-color: #ff5f86;
  color: white;
}
.no-btn, .try-again-btn {
  background-color: #4a2a1a;
  color: white;
}

.gifts-container {
  display: flex;
  gap: 30px;
  margin-top: 20px;
}
.gift-box {
  width: 150px;
  height: 150px;
  cursor: pointer;
  transition: transform 0.3s;
}
.gift-box:hover {
  transform: translateY(-10px) scale(1.1);
}

.back-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  padding: 10px 20px;
  background: transparent;
  border: 2px solid #d4235c;
  color: #d4235c;
  border-radius: 20px;
  font-size: 1rem;
  cursor: pointer;
  font-weight: bold;
}

.card-layout {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 40px;
  width: 100%;
}
.card-text {
  flex: 1;
  text-align: left;
}
.card-photo img {
  width: 250px;
  height: 300px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.polaroid-container {
  display: flex;
  gap: 20px;
  margin: 30px 0;
}
.polaroid {
  background: white;
  padding: 10px 10px 30px 10px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
  transform: rotate(-5deg);
}
.polaroid:nth-child(2) { transform: rotate(3deg) translateY(-10px); }
.polaroid:nth-child(3) { transform: rotate(-2deg); }
.polaroid img {
  width: 150px;
  height: 150px;
  object-fit: cover;
}
.polaroid .caption {
  margin-top: 10px;
  font-size: 1.5rem;
  color: #d4235c;
}

.letter-content {
  text-align: left;
  max-width: 600px;
  font-size: 1.2rem;
  line-height: 1.5;
  color: #4a2a1a;
  overflow-y: auto;
  max-height: 50vh;
  padding: 20px;
}

"""

with open('birthday.css', 'w', encoding='utf-8') as f:
    f.write(css[:start_idx] + new_css + css[end_idx:])
