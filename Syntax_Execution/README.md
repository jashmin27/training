# 4.1 Syntax & Execution — 20 Programs

Covers: variables, types, expressions, operators, input/output, comments,
indentation, script execution, modules and imports.

## Folder structure

```
python_fundamentals/
├── calculator/            (4 programs)
│   ├── calculator_basic.py         - basic +,-,*,/
│   ├── calculator_functions.py     - refactored into functions
│   └── calculator_dict_ops.py      - operations stored in a dict of lambdas
│
├── unit_converter/         (4 programs)
│   ├── convert_length.py           - km <-> miles, meters <-> feet
│   ├── convert_temperature.py      - Celsius <-> Fahrenheit/Kelvin
│   ├── convert_weight.py           - kg <-> lb/grams
│   └── convert_multi.py            - menu-driven, combines all conversions
│
├── grade_calculator/       (4 programs)
│   ├── grade_single.py             - one subject -> letter grade
│   ├── grade_average.py            - average across several subjects
│   ├── grade_gpa.py                - credit-weighted GPA
│   └── grade_letter.py             - lookup-table based grading function
│
├── menu_cli/                (4 programs)
│   ├── menu_calculator.py          - looping calculator menu
│   ├── menu_todo.py                - add/view/remove to-do list
│   ├── menu_number_utils.py        - even/odd, prime check, factorial
│   └── menu_dashboard.py           - combined grade + converter dashboard
│
└── text_formatter/          (4 programs)
    ├── format_case.py              - upper/lower/title/capitalize/swapcase
    ├── format_stats.py             - word/character/sentence counts
    ├── format_cleaner.py           - strip spaces & punctuation
    └── format_advanced.py          - reverse, padding, palindrome check
```

## How to run any program

```bash
python3 calculator/calculator_basic.py
```

Each file:
- has a docstring at the top naming the concepts it demonstrates
- is self-contained and runnable on its own
- uses `input()` for interaction, so just follow the prompts

## Self-check before moving to 4.2

- Can you explain what `float(input(...))` is doing in two steps?
- Which programs use functions vs. plain top-to-bottom script style?
- In `calculator_dict_ops.py`, what is a lambda and why store functions in a dict?
- In `convert_multi.py`, why does the `while True` loop need a `break`?
