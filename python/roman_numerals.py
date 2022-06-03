def to_roman(num):
    import math
    arab = num
    answer = []
    romans_obj = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }
    
    for  roman in romans_obj :   

        arab = math.floor(num / romans_obj[roman])
        num -= arab * romans_obj[roman] 
        answer += roman * arab    
        
    answer = "".join(answer)

    return answer