# Algebra Solver

A Python CLI tool for solving algebraic equations, simplifying expressions, factoring, and expanding.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Run the interactive solver:

```bash
python main.py
```

### Commands

| Command | Description | Example |
|---------|-------------|---------|
| `solve` | Solve an equation | `solve 2x + 3 = 7` |
| `system` | Solve a system of equations | Enter equations interactively |
| `simplify` | Simplify an expression | `simplify (x^2 - 1) / (x - 1)` |
| `factor` | Factor an expression | `factor x^2 + 5x + 6` |
| `expand` | Expand an expression | `expand (x + 2)(x + 3)` |

### Examples

```
algebra> solve 2x + 3 = 7
  Variable: x
  Solution: 2

algebra> solve x^2 - 5x + 6 = 0
  Variable: x
  Solutions: 2, 3

algebra> factor x^2 + 5x + 6
  x**2 + 5*x + 6  →  (x + 2)*(x + 3)

algebra> expand (x + 2)(x + 3)
  (x + 2)*(x + 3)  →  x**2 + 5*x + 6

algebra> simplify (x^2 - 1) / (x - 1)
  (x**2 - 1)/(x - 1)  →  x + 1
```

### Solving a system of equations

```
algebra> system
  Enter equations one per line (blank line to finish):
    eq> x + y = 10
    eq> x - y = 2
    eq>

  Variables: x, y
  Solutions: {x: 6, y: 4}
```

## Using as a library

You can also import the solver directly:

```python
from solver import solve_equation, solve_system, simplify_expression

result = solve_equation("2x + 3 = 7")
print(result["solutions"])  # ['2']
```
