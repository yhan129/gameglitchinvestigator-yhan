# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
game seems nice looking but buggy.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
game was broken. go "lower / higher" seems to be mixed up
could not restart the game after it was over
the range does not change correctly 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Bug	Fix
Higher/Lower swapped	guess > secret → "Go LOWER", guess < secret → "Go HIGHER"
Can't restart	New Game now resets status back to "playing"
Range ignores difficulty	Hard changed to 1-1000; New Game uses randint(low, high)
Hint text hardcoded	Info message now shows {low} and {high} dynamically
(Bonus) String comparison bug	Removed the even/odd str() conversion that broke comparisons

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
AI thought low/high logic was correct at first. I had to guide it.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I have tried playing it. it works as it should now.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
Trying low number and high number while knowing the secret number.
when I make the right guess, it recognizes it.
- Did AI help you design or understand any tests? How?
It did but I already had underatsnding of where it was causing the issue.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Without session state, random.randint(low, high) ran again every rerun, generating a new secret each time
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
every button click refreshes the whole page like a browser reload.
all your variables reset to zero. Session state is like a sticky notepad that survives those reloads.
- What change did you make that finally gave the game a stable secret number?
New Game button was calling random.randint(1, 100) 
so changed it to randint(low, high)
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Always read the code before trusting the output.
- What is one thing you would do differently next time you work with AI on a coding task?
Run pytest first before playing manually. The test file was already there and would have caught the broken functions immediately instead of discovering bugs one by one through play.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code can look clean and complete while hiding subtle logic bugs. You still need to read and test it like any other code — the fact that AI wrote it does not make it correct.
