class RomanConverter:
    def __init__(self, number):
        self.number = number
        self.roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    def to_roman(self):
        result = ''
        num = self.number
        for value, numeral in self.roman_numerals:
            while num >= value:
                result += numeral
                num -= value
        return result
number=int(input('What is the number: '))
converter = RomanConverter(number)
print(converter.to_roman())
