from sympy import symbols, sympify, Eq, solve, simplify, expand, factor
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor,
)


def _parse(expr_str: str):
    """Parse a string into a sympy expression, supporting implicit
    multiplication (e.g. '2x') and caret for exponentiation ('x^2')."""
    return parse_expr(expr_str.strip(), transformations=TRANSFORMATIONS)


def _detect_symbols(expr):
    """Return the free symbols sorted alphabetically by name."""
    return sorted(expr.free_symbols, key=lambda s: s.name)


def solve_equation(equation_str: str) -> dict:
    """Solve a single algebraic equation given as a string.

    Supports forms like:
        '2x + 3 = 7'
        'x^2 - 4 = 0'
        'x^2 + 5x + 6'   (implicitly set equal to 0)

    Returns a dict with 'variable', 'solutions', and 'steps'.
    """
    steps: list[str] = []
    steps.append(f"Input: {equation_str}")

    if "=" in equation_str:
        lhs_str, rhs_str = equation_str.split("=", 1)
        lhs = _parse(lhs_str)
        rhs = _parse(rhs_str)
        equation = Eq(lhs, rhs)
        expr = lhs - rhs
        steps.append(f"Parsed equation: {lhs} = {rhs}")
        steps.append(f"Rearranged to: {simplify(expr)} = 0")
    else:
        expr = _parse(equation_str)
        equation = Eq(expr, 0)
        steps.append(f"Parsed expression: {expr}")
        steps.append("Set equal to 0 (no '=' found)")

    syms = _detect_symbols(expr)
    if not syms:
        raise ValueError("No variables found in the equation.")

    var = syms[0]
    steps.append(f"Solving for: {var}")

    solutions = list(filter(None, solve(equation, var)))
    steps.append(f"Solutions: {', '.join(str(s) for s in solutions)}")

    return {
        "variable": str(var),
        "solutions": [str(s) for s in solutions],
        "steps": steps,
    }


def solve_system(equations: list[str]) -> dict:
    """Solve a system of equations.

    Each equation string may use '=' or be implicitly set to 0.
    Returns a dict with 'variables', 'solutions', and 'steps'.
    """
    steps: list[str] = []
    eqs = []

    for eq_str in equations:
        if "=" in eq_str:
            lhs_str, rhs_str = eq_str.split("=", 1)
            lhs, rhs = _parse(lhs_str), _parse(rhs_str)
            eqs.append(Eq(lhs, rhs))
            steps.append(f"  {lhs} = {rhs}")
        else:
            expr = _parse(eq_str)
            eqs.append(Eq(expr, 0))
            steps.append(f"  {expr} = 0")

    all_syms = set()
    for eq in eqs:
        all_syms |= eq.free_symbols
    var_list = sorted(all_syms, key=lambda s: s.name)

    steps.insert(0, "System of equations:")
    steps.append(f"Variables: {', '.join(str(v) for v in var_list)}")

    solutions = solve(eqs, var_list)
    steps.append(f"Solutions: {solutions}")

    if isinstance(solutions, dict):
        formatted = {str(k): str(v) for k, v in solutions.items()}
    elif isinstance(solutions, list):
        formatted = [
            {str(var_list[i]): str(val) for i, val in enumerate(tup)}
            if isinstance(tup, tuple)
            else str(tup)
            for tup in solutions
        ]
    else:
        formatted = str(solutions)

    return {
        "variables": [str(v) for v in var_list],
        "solutions": formatted,
        "steps": steps,
    }


def simplify_expression(expr_str: str) -> dict:
    """Simplify an algebraic expression."""
    expr = _parse(expr_str)
    result = simplify(expr)
    return {
        "original": str(expr),
        "simplified": str(result),
    }


def factor_expression(expr_str: str) -> dict:
    """Factor an algebraic expression."""
    expr = _parse(expr_str)
    result = factor(expr)
    return {
        "original": str(expr),
        "factored": str(result),
    }


def expand_expression(expr_str: str) -> dict:
    """Expand an algebraic expression."""
    expr = _parse(expr_str)
    result = expand(expr)
    return {
        "original": str(expr),
        "expanded": str(result),
    }
