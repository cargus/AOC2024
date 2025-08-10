"""
Advent of Code Day 2 Problem: Read in lines of varying length from an input file to check if they are consistently
increasing or decreasing. The increase or decrease also cannot be greater than 3. Lines that meet these standards are
considered "safe reports". There is also a tolerance limit of 1, meaning 1 single report can break the trend in any way
and the report still be considered safe. As long as removing that single data point allows the rest to follow the
correct trend.
"""

"""
name: is_safe
parameters: readings, tolerance
return: Is string safe (Boolean)
purpose: Check if input string is consistently increasing or decreasing by 3 or less.
"""
def is_safe(readings: list[str], tolerance: int = 0) -> bool:
    #get the number of numbers in the list
    #The subtract one is because of using i +1 for the difference, without you get an overflow error.
    length = len(readings) - 1
    # set the default levels for variables
    i = 0
    direction = ""
    difference = int(readings[i]) - int(readings[i + 1])
    status = ""

    #check for a positive or negative difference and assign direction, if zero, this fails
    if difference < 0:
        direction = "down"
    if difference > 0:
        direction = "up"

    #check the rest of the numbers follow the down direction by no more than 3
    while i < length and direction == "down":
        difference = int(readings[i]) - int(readings[i + 1])
        if -4 < difference < 0:
            status = "pass"
        else:
            status = ""
            break
        i += 1

    #check the rest of the numbers follow the up direction by no more than 3
    while i < length and direction == "up":
        difference = int(readings[i]) - int(readings[i + 1])
        if 0 < difference < 4:
            status = "pass"
        else:
            status = ""
            break
        i += 1

    #return true if all numbers pass the rules
    if status == "pass":
        return True

    #logic handling for one "bad reading"
    elif tolerance == 0:
        #remove the "bad reading" and create a new list without that number, determine if it now passes
        for counter in range(len(readings)):
            new_list = list(readings)
            del new_list[counter]
            if is_safe(new_list, 1):
                print(readings)
                print("true")
                return True
        #returns false if the new list breaks any of the rules
        return False
    #returns false if one measurement has already been removed
    return False

def __main__():
    # open input file and read in lines
    with open('inputs/day2_input.txt', 'r') as file:
        content = file.read().splitlines()
    # set # of safe reports to zero
    safe_reports = 0

    #handle logic for each line
    for line in content:
        # split string on spaces
        line_input = line.split(" ")
        #run the is safe function and if returns true, increase the safe reports count by 1
        if is_safe(line_input, 0):
            safe_reports +=1
    # output the number of safe reports in the report
    print(f"The number of safe reports is {safe_reports}")

__main__()
