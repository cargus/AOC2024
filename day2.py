with open('./day2_input.txt', 'r') as file:
    content = file.read().splitlines()
safe_reports = 0

for line in content:
    readings = line.split(" ")
    num = len(readings)-1
    i = 0
    direction = ""
    difference = int(readings[i]) - int(readings[i+1])
    status = ""
    if difference == 0:
        i += 1
        continue
    if difference < 0:
        direction = "down"
    if difference > 0:
        direction = "up"
    while i < num and direction=="down":
        difference = int(readings[i]) - int(readings[i + 1])
        if readings[i] == readings[i+1]:
            i += 1
            status = ""
            break
        if 0 > difference > -4:
            i += 1
            status = "pass"
            continue
        else:
            status  = ""
            break
    while i < num and direction =="up":
        difference = int(readings[i]) - int(readings[i + 1])
        if readings[i] == readings[i+1]:
            i += 1
            status = ""
            break
        if  0 < difference < 4:
            i += 1
            status = "pass"
            continue
        else:
            status = ""
            break
    while i == num:
        if status =="pass":
            safe_reports += 1
        i +=1
    else:
        safe_reports = safe_reports
        i =+ i
        continue
print (safe_reports)