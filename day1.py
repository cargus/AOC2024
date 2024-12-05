with open('inputs/day1_input.txt', 'r') as file:
    content = file.read().splitlines()

column_1 = []
column_2 = []
for line in content:
    column_1.append(line.split("   ")[0])
    column_2.append(line.split("   ")[1])
column_1.sort()
column_2.sort()

sort_list = list(zip(column_1, column_2))
total = 0
for line in sort_list:
    total = total + (abs(int(line[0]) - int(line[1])))
print("Part 1 answer is " + str(total))

new_list = []

for line in column_1:
    multiplier = 0
    value = int(line)
    for checkline in column_2:
        check = int(checkline)
        if value == check:
            multiplier+=1
    new_list.append(int(multiplier) * int(value))
print("Part 2 answer is " + str(sum(new_list)))

