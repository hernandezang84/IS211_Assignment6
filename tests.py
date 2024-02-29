import unittest
from conversions import convertCelsiusToKelvin, convertCelsiustoFahrenheit, convertFahrenheitToCelsius, convertFahrenheitToKelvin, convertKelvinToCelsius, convertKelvinToFahrenheit

class TestCelsiusConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (-273.15, 0),
            (30, 303.15),
            (300, 573.15),
        ]
        for celsius, expected in test_cases:
            result = convertCelsiusToKelvin(celsius)
            self.assertEqual(result, expected, f"Failed to convert {celsius}°C to {expected}K")

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (30, 86),
            (300, 572),
        ]
        for celsius, expected in test_cases:
            result = convertCelsiustoFahrenheit(celsius)
            self.assertEqual(result, expected, f"Failed to convert {celsius}°C to {expected}°F")

    def test_convertFahrenheitToCelsius(self):
        test_cases = [
            (32, 0),
            (212, 100),
            (-40, -40),
            (86, 30),
            (572, 300),
        ]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(result, expected, f"Failed to convert {fahrenheit}°F to {expected}°C")

    def test_convertFahrenheitToKelvin(self):
        test_cases = [
            (32, 273.15),
            (212, 373.15),
            (-40, 233.15),
            (86, 303.15),
            (572, 573.15),
        ]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            self.assertAlmostEqual(result, expected, places=7, msg=f"Failed to convert {fahrenheit}°F to {expected}K")

    def test_convertKelvinToCelsius(self):
        test_cases = [
            (273.15, 0),
            (373.15, 100),
            (233.15, -40),
            (303.15, 30),
            (573.15, 300),
        ]
        for kelvin, expected in test_cases:
            result = convertKelvinToCelsius(kelvin)
            self.assertAlmostEqual(result, expected, places=7, msg=f"Failed to convert {kelvin}K to {expected}°C")

    def test_convertKelvinToFahrenheit(self):
        test_cases = [
            (273.15, 32),
            (373.15, 212),
            (233.15, -40),
            (303.15, 86),
            (573.15, 572),
        ]
        for kelvin, expected in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            self.assertAlmostEqual(result, expected, places=7, msg=f"Failed to convert {kelvin}K to {expected}°F")

if __name__ == '__main__':
    unittest.main()