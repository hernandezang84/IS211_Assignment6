import unittest
from conversions_refactored import convert, ConversionNotPossible

class TestConversionsRefactored(unittest.TestCase):
    def test_temperature_conversions(self):
        temp_tests = [
            ('Celsius', 'Fahrenheit', 100, 212),
            ('Celsius', 'Kelvin', 100, 373.15),
            ('Fahrenheit', 'Celsius', 32, 0),
            ('Fahrenheit', 'Kelvin', 212, 373.15),
            ('Kelvin', 'Celsius', 273.15, 0),
            ('Kelvin', 'Fahrenheit', 273.15, 32),
        ]
        for from_unit, to_unit, value, expected in temp_tests:
            result = convert(from_unit, to_unit, value)
            self.assertAlmostEqual(result, expected, places=7, msg=f"Failed converting {from_unit} to {to_unit}")

    def test_distance_conversions(self):
        distance_tests = [
            ('Miles', 'Yards', 1, 1760),
            ('Miles', 'Meters', 1, 1609.34),
            ('Yards', 'Miles', 1760, 1),
            ('Yards', 'Meters', 1, 0.9144),
            ('Meters', 'Miles', 1609.34, 1),
            ('Meters', 'Yards', 1, 1/0.9144),
        ]
        for from_unit, to_unit, value, expected in distance_tests:
            result = convert(from_unit, to_unit, value)
            self.assertAlmostEqual(result, expected, places=7, msg=f"Failed converting {from_unit} to {to_unit}")

    def test_identity_conversion(self):
        units = ['Celsius', 'Fahrenheit', 'Kelvin', 'Miles', 'Yards', 'Meters']
        value = 100
        for unit in units:
            result = convert(unit, unit, value)
            self.assertEqual(result, value, f"Failed identity conversion for {unit}")

    def test_incompatible_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert('Celsius', 'Meters', 100)
        with self.assertRaises(ConversionNotPossible):
            convert('Miles', 'Kelvin', 5)

if __name__ == '__main__':
    unittest.main()