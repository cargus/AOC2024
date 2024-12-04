#check Second letter and determine direction
def check_letter (row_d,col_d, letter, list_out, compass):
    if -1< row_d < int(n_rows-1) and -1 < col_d < int(n_columns) and content[int(row_d)] [int(col_d)] == letter:
        list_out[row_d,col_d] = compass
        return list_out

#check letters after direction determined
def check_letter_direction (row_d, col_d, letter, list_out, compass):
    if -1 < row_d < int(n_rows-1) and -1 < col_d < int(n_columns) and direction == compass and content[int(row_d)][int(col_d)] == letter:
        list_out[row_d, col_d] = direction

#open input file
with open('inputs/day4_input.txt', 'r') as file:
    content = file.read().splitlines()

#setup lists/ dictionaries for letter coordinates
X_list = []
M_list = {}
A_list = {}
S_list = {}

#get size of the word search
n_rows = len(content)
column_count = [len(string) for string in content]
n_columns = column_count[0]

#find coordinates of all X's in the word search
for row_index, line in enumerate(content):
    for col_index, character in enumerate (line):
            if character == "X":
                coordinates = row_index, col_index
                X_list.append(coordinates)
print ("the number of Xs is " + str(len(X_list)))
print (X_list)

#get list of Ms by the Xs and determine direction
for row , col in X_list:
#define all coordinates to look at
    col_N = col
    row_N = row-1
    col_NE = col+1
    row_NE = row-1
    col_E = col+1
    row_E = row
    row_SE = row+1
    col_SE = col+1
    col_S = col
    row_S = row+1
    col_SW = col-1
    row_SW = row+1
    col_W = col-1
    row_W = row
    row_NW = row-1
    col_NW = col-1

#check all coordinates for letter M
    check_letter(row_N,col_N,"M", M_list,"N")
    check_letter(row_NE,col_NE,"M", M_list,"NE")
    check_letter(row_E,col_E,"M", M_list,"E")
    check_letter(row_SE,col_SE,"M", M_list,"SE")
    check_letter(row_S,col_S,"M", M_list,"S")
    check_letter(row_SW,col_SW,"M", M_list,"SW")
    check_letter(row_W,col_W,"M", M_list,"W")
    check_letter(row_NW,col_NW,"M", M_list,"NW")
print ("the number of Ms is " + str(len(M_list)))
print (M_list)

#get list of As by the Ms and following direction
for coordinates , direction in M_list.items():
#clean up X and Y coordinates from the dictionary list
    row_col = str(coordinates).split(", ")
    row = row_col[0].lstrip('(')
    row = int(row)
    col = row_col[1].rstrip(')')
    col = int(col)

#define all coordinates to look at
    col_N = col
    row_N = row - 1
    col_NE = col + 1
    row_NE = row - 1
    col_E = col + 1
    row_E = row
    row_SE = row + 1
    col_SE = col + 1
    col_S = col
    row_S = row + 1
    col_SW = col - 1
    row_SW = row + 1
    col_W = col - 1
    row_W = row
    row_NW = row - 1
    col_NW = col - 1
#check all coordinates for letter A
    check_letter_direction(row_N, col_N, "A", A_list, "N")
    check_letter_direction(row_NE, col_NE, "A", A_list, "NE")
    check_letter_direction(row_E, col_E, "A", A_list, "E")
    check_letter_direction(row_SE, col_SE, "A", A_list, "SE")
    check_letter_direction(row_S, col_S, "A", A_list, "S")
    check_letter_direction(row_SW, col_SW, "A", A_list, "SW")
    check_letter_direction(row_W, col_W, "A", A_list, "W")
    check_letter_direction(row_NW, col_NW, "A", A_list, "NW")

#get count of Ss by the As and following direction
for coordinates , direction in A_list.items():
#clean up X and Y coordinates from the dictionary list
    row_col = str(coordinates).split(", ")
    row = row_col[0].lstrip('(')
    row = int(row)
    col = row_col[1].rstrip(')')
    col = int(col)

# define all coordinates to look at
    col_N = col
    row_N = row - 1
    col_NE = col + 1
    row_NE = row - 1
    col_E = col + 1
    row_E = row
    row_SE = row + 1
    col_SE = col + 1
    col_S = col
    row_S = row + 1
    col_SW = col - 1
    row_SW = row + 1
    col_W = col - 1
    row_W = row
    row_NW = row - 1
    col_NW = col - 1
#check all coordinates for letter S
    check_letter_direction(row_N, col_N, "S", S_list, "N")
    check_letter_direction(row_NE, col_NE, "S", S_list, "NE")
    check_letter_direction(row_E, col_E, "S", S_list, "E")
    check_letter_direction(row_SE, col_SE, "S", S_list, "SE")
    check_letter_direction(row_S, col_S, "S", S_list, "S")
    check_letter_direction(row_SW, col_SW, "S", S_list, "SW")
    check_letter_direction(row_W, col_W, "S", S_list, "W")
    check_letter_direction(row_NW, col_NW, "S", S_list, "NW")

print(len(S_list))