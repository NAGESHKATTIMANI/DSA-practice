def romanToInt(s: str) -> int:
    mapping ={
        'I'   :          1,
        'V'             :5,
        'X'             :10,
        'L'             :50,
        'C'             :100,
        'D'             :500,
        'M'             :1000
    }
    result = 0
    for index in range(len(s)):
        if index < len(s)-1 and mapping[s[index]] < mapping[s[index + 1]]:
            result -= mapping[s[index]]
        else:
            result += mapping[s[index]]
    return result

roman = "III"
print(romanToInt(roman))