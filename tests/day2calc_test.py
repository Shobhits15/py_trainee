
import unittest

from day2calc import calculate_avg, calculate_grade


class TestCalculator(unittest.TestCase):
    def test_average(self):
        self.assertEqual(calculate_avg([80, 90, 100]), 90)


    def test_grade(self):
        cases = [
            (95, "A"),
            (90, "A"),
            (75, "B"),
            (60, "B"),
            (59, "C"),
            (0, "C"),
        ]
        for average, expected_grade in cases:
            with self.subTest(average=average):
                self.assertEqual(calculate_grade(average), expected_grade)


    def test_empty_marks(self):
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            calculate_avg([])


    def test_invalid_marks(self):
        for invalid_mark in [-1, 101]:
            with self.subTest(invalid_mark=invalid_mark):
                with self.assertRaisesRegex(ValueError, "between 0 and 100"):
                    calculate_avg([80, invalid_mark])