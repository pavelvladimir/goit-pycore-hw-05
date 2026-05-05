import types
import unittest

from goit_pycore_hw_05 import generator_numbers, sum_profit


class ProfitGeneratorTests(unittest.TestCase):
    def test_generator_numbers_returns_generator(self):
        result = generator_numbers("Income 10.5 and 20.25")

        self.assertIsInstance(result, types.GeneratorType)

    def test_generator_numbers_yields_expected_values(self):
        text = (
            "Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями "
            "27.45 і 324.00 доларів."
        )

        result = list(generator_numbers(text))

        self.assertEqual(result, [1000.01, 27.45, 324.00])

    def test_generator_numbers_supports_integers_and_signed_values(self):
        text = "Values 10 -5 2.5 +3.5 end"

        result = list(generator_numbers(text))

        self.assertEqual(result, [10.0, -5.0, 2.5, 3.5])

    def test_generator_numbers_ignores_numbers_attached_to_other_symbols(self):
        text = "Bad:10.5 20.0, (30.0) good 40.0"

        result = list(generator_numbers(text))

        self.assertEqual(result, [40.0])

    def test_sum_profit_returns_total(self):
        text = (
            "Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями "
            "27.45 і 324.00 доларів."
        )

        result = sum_profit(text, generator_numbers)

        self.assertAlmostEqual(result, 1351.46, places=2)

    def test_sum_profit_returns_zero_when_no_numbers_are_found(self):
        result = sum_profit("There is no income data here.", generator_numbers)

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
