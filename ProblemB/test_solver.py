import unittest
from solver import solve

class TestAlgebraSolver(unittest.TestCase):
    def test_3x_eq_0(self):
        # Equation: 3x = 0
        solutions = solve('3x = 0')
        self.assertTrue(any(abs(sol) < 1e-6 for sol in solutions), "Should find x=0 as a solution")
        # Check for no extraneous solutions
        for sol in solutions:
            self.assertTrue(abs(sol) < 1e-6, f"Unexpected solution: {sol}")

if __name__ == "__main__":
    unittest.main()
