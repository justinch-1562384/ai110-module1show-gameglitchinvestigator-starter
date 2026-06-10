# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran the game, I saw the following screen. I was given a prompt where I have to guess a number between 1 and 100. 
  ![initial screen](image.png)

Concrete Bug #1: The "Show hint" button does not have the same styling as the other new buttons ("Submit Guess" and "New Game")

Concrete Bug #2: The Attempts allowed on the left hand side of the screen does not match the attempts left in the prompt (8 vs 7)

Concrete Bug #3: Clicking on the New Game Button did not reset the game to its initial state. 

Concrete Bug #4: Using the Enter button into the "Enter your guess:" box does not make a submission to the 

Concrete Bug #5: Negative numbers specified count as an attempt and are recorded.

Concrete Bug #6: Numbers over the specified range (i.e 100)


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|-1|The program would mark this as an invalid value|This program marks this as a valid value| None |
| 10000 | The program would mark this as an invalid value| This program marks this as a valid value | None |
| Enter into text box | The program would process the action similiar to when we click on Submit guess | No action is recorded from the program  | None |
| 30 | The text box would list it as "Go Lower" | The text box mentions it as going higher | Go HIGHER! (Answer is listed as 19) |
| 23 | The text box would list it as "Go Higher" | The text box mentions it as going Lower | Go LOWER! (Answer is listed as 94) |
| Off by One | When starting the project, one of the guesses is already used. This is seen in the Attempts left for Normal as an example. | Attempts left != Attempts allowed in sidebar | None |
| Clicking on New Game | Once clicked, a new game would be available, resetting it to what was it initially on startup | it stayed the same, requiring the entire application to be refreshed | Error |
| 1.52 | It should default to the higher number (In this case, 2 should be entered) or be marked as invalid | This was marked in history under 1 | Marked as 1 in History |
| Switching difficulty | Switching difficulty should generate a new secret number, reset the attempts, and notify the user that this was done | The same secret is still set, the number of attempts allowed/already guessed does not change | Error |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
