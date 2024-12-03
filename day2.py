


def is_safe(readings: list[str], tolerance: int = 0) -> bool:
    num = len(readings) - 1
    i = 0
    direction = ""
    difference = int(readings[i]) - int(readings[i + 1])
    status = ""
    if difference == 0:
        i += 1
        return False
    if difference < 0:
        direction = "down"
    if difference > 0:
        direction = "up"
    while i < num and direction == "down":
        difference = int(readings[i]) - int(readings[i + 1])
        if difference in [-1, -2, -3]:
            status = "pass"
        else:
            status = ""
            break
        i += 1
    while i < num and direction == "up":
        difference = int(readings[i]) - int(readings[i + 1])
        if difference in [1, 2, 3]:
            status = "pass"
        else:
            status = ""
            break
        i += 1
    if status == "pass":
        return True
    elif tolerance == 0:
        for counter in range(len(readings)):
            new_list = list(readings)
            del new_list[counter]
            if is_safe(new_list, tolerance + 1):
                return True
        return False
    return False

with open('./day2_input.txt', 'r') as file:
    content = file.read().splitlines()
safe_reports = 0

for line in content:
    line_input = line.split(" ")
    if is_safe(line_input, 0):
        safe_reports +=1


print(safe_reports)
