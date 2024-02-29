class ConversionNotPossible(Exception):
    pass

def convert_temperature(fromUnit, toUnit, value):
    formulas = {
        ('Celsius', 'Fahrenheit'): lambda c: (c * 9/5) + 32,
        ('Celsius', 'Kelvin'): lambda c: c + 273.15,
        ('Fahrenheit', 'Celsius'): lambda f: (f - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda f: (f - 32) * 5/9 + 273.15,
        ('Kelvin', 'Celsius'): lambda k: k - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda k: (k - 273.15) * 9/5 + 32,
    }
    try:
        return formulas[(fromUnit, toUnit)](value)
    except KeyError:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not supported.")
    
def convert_distance(fromUnit, toUnit, value):
        rates = {
            ('Miles', 'Yards'): 1760,
            ('Miles', 'Meters'): 1609.34,
            ('Yards', 'Miles'): 1/1760,
            ('Yards', 'Meters'): 0.9144,
            ('Meters', 'Miles'): 1/1609.34,
            ('Meters', 'Yards'): 1/0.9144,
        }
        try:
            return value * rates[(fromUnit, toUnit)]
        except KeyError:
            raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not supported.")
        
def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value
    if all(unit in ['Celsius', 'Fahrenheit', 'Kelvin'] for unit in [fromUnit, toUnit]):
        return convert_temperature(fromUnit, toUnit, value)
    elif all(unit in ['Miles', 'Yards', 'Meters'] for unit in [fromUnit, toUnit]):
        return convert_distance(fromUnit, toUnit, value)
    else:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not compatible.")