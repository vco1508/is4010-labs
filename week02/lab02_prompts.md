# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

Installed and authenticated GitHub Copilot CLI successfully. Version: 1.0.83.

### Antigravity CLI

Installed and authenticated Antigravity CLI successfully. Version: 1.1.27.

## Shared task

### Shared prompt


```text
Write a Python function count_vowels(text: str) -> int that counts the vowels a, e, i, o, u case-insensitively, and never counts y as a vowel.
```

### Copilot CLI observations

Copilot CLI didn't just answer the prompt directly — it first explored the repository, searching for existing Python files and reading lab02.md, test_lab02.py, and lab02_prompts.md to understand the assignment context. It then created week02/lab02.py itself, implementing all three required functions, including count_vowels using text.lower() combined with a check against the string "aeiou". It asked for my approval before writing the file and before running the tests. 

### Antigravity CLI observations

When given the identical prompt, Antigravity CLI returned a working count_vowels implementation directly in the terminal without exploring the repository or writing to any file. Unlike Copilot, it didn't take any extra investigative steps before answering. Its approach built a set containing both lowercase and uppercase vowels (aeiouAEIOU) and checked each character against that set, rather than normalizing case with .lower() like Copilot did. The logic is correct and would pass the same tests, but it's slightly more verbose than necessary. I'd want to verify it handles an empty string correctly, though based on the logic it clearly does, since summing over nothing returns zero.

### Comparison

Both tools produced correct implementations of count_vowels that satisfy the required contract: counting a, e, i, o, and u case-insensitively while never counting y, and correctly handling an empty string by returning zero. In terms of correctness, there's no meaningful difference — both would pass the same test cases. Clarity-wise, Copilot's approach is slightly more idiomatic: normalizing each character with .lower() and checking it against a single lowercase string "aeiou" is a common, easy-to-read pattern. Antigravity's approach works just as well but is a bit more verbose, since it explicitly lists both cases in the vowels set instead of normalizing case first. Neither made any incorrect assumptions about the input, though neither explicitly handles non-string input, which wasn't required by the contract anyway. Usefulness-wise, Copilot's version was more convenient in this workflow since it explored the repository automatically and wrote the file directly, saving me a manual step, while Antigravity required me to copy the function in myself. I ultimately kept Copilot's implementation in lab02.py, since it was already in place, passed all nine tests, and reads slightly cleaner.

## Test-guided implementation

After Copilot CLI generated week02/lab02.py, I ran the test suite with pytest before assuming the code was correct. All nine tests passed on the first attempt, covering make_greeting with simple and multi-word names, is_even across positive, negative, and zero values, and count_vowels for mixed-case text and empty strings. Rather than treating that as the end of the process, I manually traced through count_vowels against a few cases by hand, including "rhythms" (no vowels, since y doesn't count) and an empty string, to confirm the .lower() and "aeiou" membership check behaved as expected beyond what the automated tests covered. No revision was needed since the initial implementation matched the function contracts exactly, but I used the passing tests plus my own inspection, not just Copilot's say-so, to decide the code was actually correct before committing it.

## Preferred tool combination

Comparing all four options I've used so far, each fits a different part of my workflow. Browser chat is useful for quick conceptual questions or drafting text like this journal, but it can't touch my actual files. GitHub Copilot in VS Code is best for small, in-context suggestions while I'm actively typing, since it doesn't require switching to a separate terminal session. Copilot CLI proved the most convenient for this lab specifically, since it explored the repository on its own, found the right file to edit, and ran the tests after I approved its changes, cutting out several manual steps. Antigravity CLI was faster to get a direct answer from since it didn't take extra investigative steps, but that also meant I had to manually place its code into the right file myself. Right now I'd lean toward Copilot CLI for repository-aware tasks like this one, but if I were working somewhere with stricter policies against letting an agent read and write files automatically, I'd switch to using a browser chat or Antigravity's more contained, print-only responses instead.
