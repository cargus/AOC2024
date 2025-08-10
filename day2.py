"""
Advent of Code Day 2 Problem: Read in lines of varying length from an input file to check if they are consistently
increasing or decreasing. The increase or decrease also cannot be greater than 3. Lines that meet these standards are
considered "safe reports". There is also a tolerance limit of 1, meaning 1 single report can break the trend in any way
and the report still be considered safe. As long as removing that single data point allows the rest to follow the
correct trend.
"""

"""
name: check_report_consistency
parameters: readings - the list of readings to be checked
return: true if report consistently incrementing, false if not
purpose: check if the list of numbers passed in is consistently incrementing by no more than 3
"""
def check_report_consistency(readings:[int])-> bool:
    i=0
    # length has 1 subtracted to prevent an overflow error due to using i + 1 for the difference
    while i < len(readings) - 1:
        difference = int(readings[i + 1]) - int(readings[i])
        if 0 < difference < 4:
            i += 1
            continue
        else:
            return False
    return True

"""
name: is_safe
parameters: readings - the list of readings to be checked
            tolerance - True means a number has been removed, tolerance has been applied to readings
return: Is string safe (Boolean)
purpose: Check if input string is consistently increasing or decreasing by 3 or less.
"""
def is_safe(readings: list[int], tolerance: bool = False) -> bool:
    #finding the difference of the first two integers to determine the expected direction
    difference = readings[1] - readings[0]

    #reverse list if descending
    if difference < 0:
        readings.reverse()

    #Checks for report consistently incrementing and returns True if it is and then ends function with True
    if check_report_consistency(readings):
        return True

    #logic handling for one "bad reading"
    if not tolerance:
        #create new list without one reading, determine if it now passes for each index
        for counter in range(len(readings)):
            new_list = list(readings)
            del new_list[counter]
            if is_safe(new_list, True):
                return True
    #returns false if one measurement being removed does not result in a valid list
    return False

def __main__():
    with open('inputs/day2_input.txt', 'r') as file:
        content = file.read().splitlines()

    # tracking of number of safe reports
    safe_reports = 0
    for line in content:
        line_input = line.split(" ")

        #convert all values to ints to allow numeric comparisons
        reading = []
        for num in line_input:
            reading.append(int(num))

        if is_safe(reading):
            safe_reports +=1

    print(f"The number of safe reports is {safe_reports}")

__main__()
