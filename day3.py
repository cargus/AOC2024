with open('./day3_input.txt', 'r') as file:
    content = file.read()
    import re
    mul_instructions = re.findall("(mul\([0-9]*,[0-9]*\))", content)
    print(mul_instructions)
    total = 0
    clean_instructions = {}
    for sets in mul_instructions:
        clean_numbers= sets.replace('mul(','')
        clean_numbers= clean_numbers.replace(')','')
        clean_numbers = clean_numbers.split(',')
        total = total + (int(clean_numbers[0]) * int(clean_numbers[1]))
print (total)