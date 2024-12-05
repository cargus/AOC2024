# check Second letter and determine direction
def letter_search(row_d, col_d, letter, coordinates):
    row = int(coordinates[0]) + int(row_d)
    col = int(coordinates[1]) + int(col_d)
    if row not in range(len(content)) or col not in range(len(content[0])):
        return None
    if content[int(row)][int(col)] == letter:
        new_coordinates = [row, col]
        return new_coordinates
    else:
        return None


def word_search(row_d, col_d, coordinates):
    M = letter_search(row_d, col_d, "M", coordinates)
    if M:
        A = letter_search(row_d, col_d, "S", M)
        if A:
            S = letter_search(row_d, col_d, "S", A)
            if S:
                return 1
    return 0


def X_search(row_d, col_d, coordinates):
    M = letter_search(row_d, col_d, "M", coordinates)
    if not M:
        return False
    S = letter_search(-row_d, -col_d, "S", coordinates)
    if not S:
        return False
    return True


# open input file
with open('inputs/day4_input.txt', 'r') as file:
    content = file.read().splitlines()

# setup lists/ dictionaries for letter coordinates
A_list = []
count = 0

# find coordinates of all X's in the word search
for row_index, line in enumerate(content):
    for col_index, character in enumerate(line):
        if character == "A":
            coordinates = row_index, col_index
            A_list.append(coordinates)

# get list of Ms by the Xs and determine direction
for row, col in A_list:
    coordinates = [row, col]
    NW = X_search(-1, -1, coordinates)
    SE = X_search(1, 1, coordinates)
    NE = X_search(-1, 1, coordinates)
    SW = X_search(1, -1, coordinates)
    if NW and SW:
        count +=1
    if NW and NE:
        count +=1
    if SW and SE:
        count +=1
    if NE and SE:
        count +=1

print(count)
