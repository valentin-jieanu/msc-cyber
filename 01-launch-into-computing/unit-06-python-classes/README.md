# Unit 6: From procedural to object-oriented programming

Module: Launch into Computing · Formative activity (not graded) · 23 November 2026

## Task

The tutor's announcement of 23 November 2026 asks students to:

1. Run the `Person` example in the tutor's notes (`classes.pdf`).
2. Change the name or the age, run it again and observe how the output changes.
3. Put a short code snippet, the output and a brief reflection in the e-portfolio.

## Files

| File | What it does |
|---|---|
| `person_class.py` | The `Person` class from the notes. Run 1 uses the values from the notes. Run 2 changes the name and the age. |
| `person_procedural.py` | The same behaviour without a class: a dictionary and separate functions, as in Units 1–5. |
| `output.txt` | The output of both programs. |

## How to run

```
python3 person_class.py
python3 person_procedural.py
```

Tested with Python 3.15.

## Output

```
Run 1: values from the notes
Name: Eve, Age: 30
Name: Adam, Age: 99
Name: Adam, Age: 15

Run 2: name and age changed
Name: Grace, Age: 85
Name: Alan, Age: 41
Name: Alan, Age: 42
```

When the values given to `Person(...)` change, the output changes. The code of the class stays the same. Each object keeps its own `name` and `age`, and `update_age()` changes only the object it is called on.

## Reflection

See the e-portfolio: https://valentin-jieanu.github.io/studies/launch-into-computing

## AI use

The code was prepared with AI assistance (Claude Code) from the tutor's example, then run and checked by me.
