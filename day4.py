#check Second letter and determine direction
def check_letter (x_d,y_d, letter, list_out, compass):
    if -1< x_d < int(n_columns) and -1 < y_d < int(n_rows) and content[int(x_d)] [int(y_d)] == letter:
        list_out[x_d,y_d] = compass
        return list_out

#check letters after direction determined
def check_letter_direction (X_D, Y_D, letter, list_out, compass):
    if -1 < X_D < int(n_columns) and -1 < Y_D < int(n_rows) and direction == compass and content[int(X_D)][int(Y_D)] == letter:
        list_out[X_D, Y_D] = direction

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
for lindex, line in enumerate(content):
    for rindex, character in enumerate (line):
            if character == "X":
                coordinates = lindex, rindex
                X_list.append(coordinates)
print ("the number of Xs is " + str(len(X_list)))

#get list of Ms by the Xs and determine direction
for X , Y in X_list:
#define all coordinates to look at
    X_N = X
    Y_N = Y-1
    X_NE = X+1
    Y_NE = Y-1
    X_E = X+1
    Y_E = Y
    X_SE = X+1
    Y_SE = Y+1
    X_S = X
    Y_S = Y+1
    X_SW = X-1
    Y_SW = Y+1
    X_W = X-1
    Y_W = Y
    X_NW = X-1
    Y_NW = Y-1

#check all coordinates for letter M
    check_letter(X_N,Y_N,"M", M_list,"N")
    check_letter(X_NE,Y_NE,"M", M_list,"NE")
    check_letter(X_E,Y_E,"M", M_list,"E")
    check_letter(X_SE,Y_SE,"M", M_list,"SE")
    check_letter(X_S,Y_S,"M", M_list,"S")
    check_letter(X_SW,Y_SW,"M", M_list,"SW")
    check_letter(X_W,Y_W,"M", M_list,"W")
    check_letter(X_NW,Y_NW,"M", M_list,"NW")


#get list of As by the Ms and following direction
for coordinates , direction in M_list.items():
#clean up X and Y coordinates from the dictionary list
    X_Y = str(coordinates).split(", ")
    X = X_Y[0].lstrip('(')
    X = int(X)
    Y = X_Y[1].rstrip(')')
    Y = int(Y)
#define all coordinates to look at
    X_N = X
    Y_N = Y-1
    X_NE = X+1
    Y_NE = Y-1
    X_E = X+1
    Y_E = Y
    X_SE = X+1
    Y_SE = Y+1
    X_S = X
    Y_S = Y+1
    X_SW = X-1
    Y_SW = Y+1
    X_W = X-1
    Y_W = Y
    X_NW = X-1
    Y_NW = Y-1
#check all coordinates for letter A
    check_letter_direction(X_N, Y_N, "A", A_list, "N")
    check_letter_direction(X_NE, Y_NE, "A", A_list, "NE")
    check_letter_direction(X_E, Y_E, "A", A_list, "E")
    check_letter_direction(X_SE, Y_SE, "A", A_list, "SE")
    check_letter_direction(X_S, Y_S, "A", A_list, "S")
    check_letter_direction(X_SW, Y_SW, "A", A_list, "SW")
    check_letter_direction(X_W, Y_W, "A", A_list, "W")
    check_letter_direction(X_NW, Y_NW, "A", A_list, "NW")

#get count of Ss by the As and following direction
for coordinates , direction in A_list.items():
#clean up X and Y coordinates from the dictionary list
    X_Y = str(coordinates).split(", ")
    X = X_Y[0].lstrip('(')
    X = int(X)
    Y = X_Y[1].rstrip(')')
    Y = int(Y)
#define all coordinates to look at
    X_N = X
    Y_N = Y-1
    X_NE = X+1
    Y_NE = Y-1
    X_E = X+1
    Y_E = Y
    X_SE = X+1
    Y_SE = Y+1
    X_S = X
    Y_S = Y+1
    X_SW = X-1
    Y_SW = Y+1
    X_W = X-1
    Y_W = Y
    X_NW = X-1
    Y_NW = Y-1
#check all coordinates for letter S
    check_letter_direction(X_N, Y_N, "S", S_list, "N")
    check_letter_direction(X_NE, Y_NE, "S", S_list, "NE")
    check_letter_direction(X_E, Y_E, "S", S_list, "E")
    check_letter_direction(X_SE, Y_SE, "S", S_list, "SE")
    check_letter_direction(X_S, Y_S, "S", S_list, "S")
    check_letter_direction(X_SW, Y_SW, "S", S_list, "SW")
    check_letter_direction(X_W, Y_W, "S", S_list, "W")
    check_letter_direction(X_NW, Y_NW, "S", S_list, "NW")

print(len(S_list))