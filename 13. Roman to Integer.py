
def romanToInt(s: str) -> int:
    number_mapper = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000,
    }
    roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    symbol_pointer = 0
    string_pointer = 0
    total = 0
    while symbol_pointer<len(roman_symbols):
        symbol = roman_symbols[symbol_pointer]
        if s[string_pointer:string_pointer+len(symbol)] == symbol:
            total += number_mapper[symbol]
            string_pointer+=len(symbol)
        else:
            symbol_pointer+=1
    return total
def romanToInt2(s: str) -> int:
    number_mapper = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    total = 0
    curr,prev = 0,0
    for l in s:
        curr = number_mapper[l]
        
        if prev < curr:
            total -= prev
            total += (curr - prev)

        total += curr
        prev = curr
    return total
romanToInt2("MCMXCIV")
        
        
        
