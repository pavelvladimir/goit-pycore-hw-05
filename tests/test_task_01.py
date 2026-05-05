import unittest

from goit_pycore_hw_05 import caching_fibonacci


class CachingFibonacciTests(unittest.TestCase):
    def test_returns_expected_fibonacci_values(self):
        fib = caching_fibonacci()

        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(15), 610)

    def test_handles_zero_and_negative_values(self):
        fib = caching_fibonacci()

        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(-5), 0)

    def test_raises_type_error_for_non_integer_input(self):
        fib = caching_fibonacci()

        with self.assertRaises(TypeError):
            fib("10")

    def test_uses_a_closure_based_cache(self):
        fib = caching_fibonacci()
        fib(8)

        self.assertIsNotNone(fib.__closure__)
        self.assertTrue(
            any(isinstance(cell.cell_contents, dict) for cell in fib.__closure__),
            "The fibonacci function should keep its cache inside a closure.",
        )

    def test_each_generated_function_has_its_own_cache(self):
        first_fib = caching_fibonacci()
        second_fib = caching_fibonacci()

        first_fib(10)
        second_fib(5)

        first_cache = next(
            cell.cell_contents
            for cell in first_fib.__closure__
            if isinstance(cell.cell_contents, dict)
        )
        second_cache = next(
            cell.cell_contents
            for cell in second_fib.__closure__
            if isinstance(cell.cell_contents, dict)
        )

        self.assertNotEqual(first_cache, second_cache)
        self.assertIsNot(first_cache, second_cache)


if __name__ == "__main__":
    unittest.main()
