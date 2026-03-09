# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## Document Your Experience

- Describe the game's purpose.
A number guessing game where the player tries to guess a secret number within a limited number of attempts. The difficulty setting changes both the number range and the attempt limit.

- Detail which bugs you found.
The higher/lower hints were backwards. The New Game button did not reset the game status so you could not replay after winning or losing. The Hard difficulty range was 1-50 which was easier than Normal, and the New Game button always used 1-100 regardless of difficulty. There was also a hidden bug where every even attempt converted the secret to a string, causing wrong comparison results.

- Explain what fixes you applied.
Swapped the Go HIGHER and Go LOWER messages in check_guess. Fixed the New Game button to reset status back to playing and use the correct range from the selected difficulty. Changed Hard range from 1-50 to 1-1000. Removed the string conversion bug. Moved all game logic from app.py into logic_utils.py and updated the import.

## 📸 Demo

- [<img width="820" height="979" alt="ss1" src="https://github.com/user-attachments/assets/f0d63fbf-ebee-4962-8c20-e0a7906590d6" />


## 🚀 Stretch Features

-
<img width="1120" height="391" alt="ss3" src="https://github.com/user-attachments/assets/5b53cfb2-1053-4128-9ca1-6adaa42baa13" />
<img width="1763" height="1078" alt="ss2" src="https://github.com/user-attachments/assets/50b2031f-ea02-442c-848e-201268afc3b8" />
