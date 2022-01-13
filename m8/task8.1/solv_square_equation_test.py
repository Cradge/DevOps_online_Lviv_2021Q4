
import unittest
import solv_square_equation


class SquareEquationTests(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(solv_square_equation.discriminant(1, 5, 6), 1)
        self.assertEqual(solv_square_equation.discriminant(1, 4, 8), -16)
        self.assertEqual(solv_square_equation.discriminant(2, 5, -7), 81)
        self.assertEqual(solv_square_equation.discriminant(16, -8, 1), 0)
        self.assertEqual(solv_square_equation.discriminant(1, -6, 9), 0)
        self.assertEqual(solv_square_equation.discriminant(1, -4, -5), 36)
        self.assertEqual(solv_square_equation.discriminant(1, 0, -3), 12)

    def test_roots(self):
        self.assertEqual(solv_square_equation.roots(1, 1, 5, 6), (-2.0, -3.0))
        self.assertEqual(solv_square_equation.roots(-16, 1, 4, 8), (None, None))
        self.assertEqual(solv_square_equation.roots(81, 2, 5, -7), (1.0, -3.5))
        self.assertEqual(solv_square_equation.roots(0, 16, -8, 1), (0.25, None))
        self.assertEqual(solv_square_equation.roots(0, 1, -6, 9), (3.0, None))
        self.assertEqual(solv_square_equation.roots(36, 1, -4, -5), (5.0, -1.0))
        self.assertEqual(solv_square_equation.roots(12, 1, 0, -3), (1.73, -1.73))

    def test_solv_square(self):
        self.assertEqual(solv_square_equation.solv_square(1, 5, 6), (-2.0, -3.0))
        self.assertEqual(solv_square_equation.solv_square(1, 4, 8), (None, None))
        self.assertEqual(solv_square_equation.solv_square(2, 5, -7), (1.0, -3.5))
        self.assertEqual(solv_square_equation.solv_square(16, -8, 1), (0.25, None))
        self.assertEqual(solv_square_equation.solv_square(1, -6, 9), (3.0, None))
        self.assertEqual(solv_square_equation.solv_square(1, -4, -5), (5.0, -1.0))
        self.assertEqual(solv_square_equation.solv_square(1, 0, -3), (1.73, -1.73))


if __name__ == '__main__':
    unittest.main()
