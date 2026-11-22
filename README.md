# password-username-generator

A console program that generates random passwords of four strengths, builds a username from your answers, and does a simple password check.

## Features

- Asks for a length, then prints four random passwords of that length: lowercase only ("Weak"), lower and upper case ("Moderate"), plus digits ("Strong"), plus symbols ("Extremely Strong").
- Builds a username from favourite colour, animal and number (in the order colour, animal, number).
- Basic weak/strong password check based on length and letter case.
- Asks for feedback and prints a thank-you message (a form link for non-positive answers).

## Tech stack

Python 3, standard library only (`random`, `time`).

## Structure

```
main.py     the whole program
README.md
LICENSE
```

## Run

```bash
python3 main.py
```

No dependencies and no environment variables. The program prints a long scripted introduction with pauses (`time.sleep`) before the first prompt, so expect about 30 seconds of waiting.

## Example

```
How long do you want your password to be? (Use numbers)12
Weak Password: qmzkdwhtbrle
...
```

## Limitations and status

- Works as a demo, but is not suitable for real passwords: it uses `random`, which is not cryptographically secure (use the `secrets` module for that).
- Input is not validated: a non-number length raises an error.
- The password checker is crude: it only looks at length and letter case, and the "good password" branch needs more than 10 characters with mixed case.
- The introduction text mentions tutorials the project was based on.

## License

MIT, see [LICENSE](LICENSE).
