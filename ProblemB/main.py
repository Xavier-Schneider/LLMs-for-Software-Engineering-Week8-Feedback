#!/usr/bin/env python3
"""Interactive CLI for the algebra solver."""

from solver import (
    solve_equation,
    solve_system,
    simplify_expression,
    factor_expression,
    expand_expression,
)

HELP_TEXT = """
╔══════════════════════════════════════════════════════════════╗
║                      Algebra Solver                         ║
╠══════════════════════════════════════════════════════════════╣
║  Commands:                                                  ║
║    solve <equation>       Solve an equation for a variable  ║
║    system                 Solve a system of equations        ║
║    simplify <expression>  Simplify an expression             ║
║    factor <expression>    Factor an expression               ║
║    expand <expression>    Expand an expression               ║
║    help                   Show this message                  ║
║    quit / exit            Exit the solver                    ║
╠══════════════════════════════════════════════════════════════╣
║  Examples:                                                  ║
║    solve 2x + 3 = 7                                         ║
║    solve x^2 - 5x + 6 = 0                                  ║
║    simplify (x^2 - 1) / (x - 1)                            ║
║    factor x^2 + 5x + 6                                      ║
║    expand (x + 2)(x + 3)                                    ║
╚══════════════════════════════════════════════════════════════╝
"""


def print_steps(steps: list[str]) -> None:
    for step in steps:
        print(f"  {step}")


def handle_solve(arg: str) -> None:
    if not arg:
        print("Usage: solve <equation>  (e.g. solve 2x + 3 = 7)")
        return
    try:
        result = solve_equation(arg)
        print(f"\n  Variable: {result['variable']}")
        if result["solutions"]:
            print(f"  Solution{'s' if len(result['solutions']) > 1 else ''}: "
                  f"{', '.join(result['solutions'])}")
        else:
            print("  No solution found.")
        print("\n  Steps:")
        print_steps(result["steps"])
    except Exception as e:
        print(f"  Error: {e}")


def handle_system() -> None:
    print("  Enter equations one per line (blank line to finish):")
    equations: list[str] = []
    while True:
        line = input("    eq> ").strip()
        if not line:
            break
        equations.append(line)
    if not equations:
        print("  No equations entered.")
        return
    try:
        result = solve_system(equations)
        print(f"\n  Variables: {', '.join(result['variables'])}")
        print(f"  Solutions: {result['solutions']}")
        print("\n  Steps:")
        print_steps(result["steps"])
    except Exception as e:
        print(f"  Error: {e}")


def handle_simplify(arg: str) -> None:
    if not arg:
        print("Usage: simplify <expression>")
        return
    try:
        result = simplify_expression(arg)
        print(f"  {result['original']}  →  {result['simplified']}")
    except Exception as e:
        print(f"  Error: {e}")


def handle_factor(arg: str) -> None:
    if not arg:
        print("Usage: factor <expression>")
        return
    try:
        result = factor_expression(arg)
        print(f"  {result['original']}  →  {result['factored']}")
    except Exception as e:
        print(f"  Error: {e}")


def handle_expand(arg: str) -> None:
    if not arg:
        print("Usage: expand <expression>")
        return
    try:
        result = expand_expression(arg)
        print(f"  {result['original']}  →  {result['expanded']}")
    except Exception as e:
        print(f"  Error: {e}")


def main() -> None:
    print(HELP_TEXT)
    while True:
        try:
            raw = input("algebra> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not raw:
            continue

        parts = raw.split(None, 1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        match cmd:
            case "solve":
                handle_solve(arg)
            case "system":
                handle_system()
            case "simplify":
                handle_simplify(arg)
            case "factor":
                handle_factor(arg)
            case "expand":
                handle_expand(arg)
            case "help":
                print(HELP_TEXT)
            case "quit" | "exit":
                print("Goodbye!")
                break
            case _:
                print(f"  Unknown command: {cmd}. Type 'help' for usage.")
        print()


if __name__ == "__main__":
    main()
