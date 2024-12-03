with open('./day3_input.txt', 'r') as file:
    content = file.read()
    import re
    dont_list = re.finditer("(don't\(\))", content)
    do_list = re.finditer("(do\(\))", content)
    mul_list = re.finditer("(mul\([0-9]*,[0-9]*\))", content)

    starts = {}
    for sets in dont_list:
        starts [sets.start()] = "dont"
    for sets in do_list:
        starts [sets.start()] = "do"
    for sets in mul_list:
        starts [sets.start()] = sets.string[sets.start():sets.end()]
    # mul_instructions = re.findall("(mul\([0-9]*,[0-9]*\))", content)
    starts = dict(sorted(starts.items()))
    total = 0
    clean_instructions = {}
    toggle = "do"
    for index, operation in starts.items():
        if operation == "do":
            toggle = "do"
        elif operation == "dont":
            toggle = "dont"
        elif toggle == "do":
            clean_numbers= operation.replace('mul(','')
            clean_numbers= clean_numbers.replace(')','')
            clean_numbers = clean_numbers.split(',')
            total = total + (int(clean_numbers[0]) * int(clean_numbers[1]))

print (total)