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
        A = letter_search(row_d, col_d, "A", M)
        if A:
            S = letter_search(row_d, col_d, "S", A)
            if S:
                return 1
    return 0


# open input file
with open('inputs/day4_input.txt', 'r') as file:
    content = file.read().splitlines()

# setup lists/ dictionaries for letter coordinates
X_list = []
count = 0

# find coordinates of all X's in the word search
for row_index, line in enumerate(content):
    for col_index, character in enumerate(line):
        if character == "X":
            coordinates = row_index, col_index
            X_list.append(coordinates)

# get list of Ms by the Xs and determine direction
for row, col in X_list:
    coordinates = [row, col]
    # North search
    count += word_search(-1, -1, coordinates)
    count += word_search(-1, 0, coordinates)
    count += word_search(-1, 1, coordinates)
    count += word_search(0, -1, coordinates)
    count += word_search(0, 1, coordinates)
    count += word_search(1, -1, coordinates)
    count += word_search(1, 0, coordinates)
    count += word_search(1, 1, coordinates)
print(count)
