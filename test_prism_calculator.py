import unittest
from prism_calculator import PrismCalculator


class TestPrismCalculator(unittest.TestCase):

    def setUp(self):
        self.length = 6
        self.width = 10
        self.height = 20

    # Test to chek if programm runs or not
    def test_program_runs(self):
        try:
            PrismCalculator.surface_area(self.length, self.width, self.height)
            PrismCalculator.volume(self.length, self.width, self.height)
        except:
            self.fail(f"Programm does not run")

    # Test for calculating total surface area of prism
    def test_surface_area(self):
        expected_area = 2 * (self.length * self.width +
                             self.width * self.height + self.height * self.length)
        self.assertEqual(PrismCalculator.surface_area(self.length, self.width, self.height),
                         expected_area, "Surface area calculation failed for valid dimensions.")

    # Test for calculating volume of prism
    def test_volume(self):
        expected_volume = self.length * self.width * self.height
        self.assertEqual(PrismCalculator.volume(self.length, self.width, self.height),
                         expected_volume, "Volume calculation failed for valid dimensions.")

    # Test when any dimension is 0 or negative value for surface area

    def test_invalid_dimensions_surface_area(self):
        try:
            PrismCalculator.surface_area(0, self.width, self.height)
            PrismCalculator.surface_area(self.length, 0, self.height)
            PrismCalculator.surface_area(self.length, self.width, 0)
        except ValueError as e:
            self.fail(
                f"ValueError raised for zero dimensions which should be valid: {e}")

        # Test with negative dimensions (should raise ValueError)
        negative_cases = [
            (self.length, -self.width, self.height),
            (self.length, self.width, -self.height),
            (-self.length, self.width, self.height)
        ]

        for dimensions in negative_cases:
            try:
                PrismCalculator.surface_area(*dimensions)
                self.fail(
                    "Expected ValueError not raised for negative dimensions.")
            except ValueError:
                pass

# Test when any dimension is 0 or negative value for surface area

    def test_invalid_dimensions_volume(self):
        try:
            PrismCalculator.volume(0, self.width, self.height)
            PrismCalculator.volume(self.length, 0, self.height)
            PrismCalculator.volume(self.length, self.width, 0)
        except ValueError as e:
            self.fail(
                f"ValueError raised for zero dimensions which should be valid: {e}")

        # Test with negative dimensions (should raise ValueError)
        negative_cases = [
            (self.length, -self.width, self.height),
            (self.length, self.width, -self.height),
            (-self.length, self.width, self.height)
        ]

        for dimensions in negative_cases:
            try:
                PrismCalculator.volume(*dimensions)
                self.fail(
                    "Expected ValueError not raised for negative dimensions.")
            except ValueError:
                pass


if __name__ == "__main__":
    unittest.main()
