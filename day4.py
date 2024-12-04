def check_letter (X,Y, X_D,Y_D, letter,list_in, list_out, compass):
    if -1< X_D < int(n_columns) and -1 < Y_D < int(n_rows) and list_in[int(X_D)] [int(Y_D)] == letter:
        list_out[X_D,Y_D] = compass
        return list_out

def check_letter_direction (X, Y, X_D, Y_D, letter, list_in, list_out, compass):
    if -1 < X_D < int(n_columns) and -1 < Y_D < int(n_rows) and direction == compass and list_in[int(X_D)][int(Y_D)] == letter:
        list_out[X_D, Y_D] = direction

with open('inputs/day4_input.txt', 'r') as file:
    content = file.read().splitlines()
    #setup lists/ dictionaries for letter coordinates
    X_list = []
    M_list = {}
    A_list = {}
    count = 0

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
print (X_list)

#get list of Ms by the Xs and determine direction
for X , Y in X_list:
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
    #check North
    check_letter(X,Y,X_N,Y_N,"M",X_list, M_list,"N")
    check_letter(X,Y,X_NE,Y_NE,"M",X_list, M_list,"NE")
    check_letter(X,Y,X_E,Y_E,"M",X_list, M_list,"E")
    check_letter(X,Y,X_SE,Y_SE,"M",X_list, M_list,"SE")
    check_letter(X,Y,X_S,Y_S,"M", X_list, M_list,"S")
    check_letter(X,Y,X_SW,Y_SW,"M", X_list, M_list,"SW")
    check_letter(X,Y,X_W,Y_W,"M", X_list, M_list,"W")
    check_letter(X,Y,X_NW,Y_NW,"M", X_list, M_list,"NW")
print (M_list)
print (len(M_list))



#get list of As by the Ms and following direction
for coordinates , direction in M_list.items():
    X_Y = str(coordinates).split(", ")
    X = X_Y[0].lstrip('(')
    X = int(X)
    Y = X_Y[1].rstrip(')')
    Y = int(Y)
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
#check North
    if -1< X_N < int(n_columns) and -1 < Y_N < int(n_rows) and direction == "N" and content[int(X_N)] [int(Y_N)] == "A":
        A_list[X_N,Y_N] = "N"
    #check North East
    if -1< X_NE < int(n_columns) and -1 < Y_NE < int(n_rows) and direction == "NE" and content[int(X_NE)] [int(Y_NE)] == "A":
        A_list[X_NE,Y_NE] = "NE"
    #check East
    if -1< X_E < int(n_columns) and -1 < Y_E < int(n_rows) and direction =="E" and content[int(X_E)] [int(Y_E)] == "A":
        A_list[X_E, Y_E] = "E"
    # check South East
    if -1< X_SE < int(n_columns) and -1 < Y_SE < int(n_rows) and direction =="SE" and content[int(X_SE)] [int(Y_SE)] == "A":
        A_list[X_SE, Y_SE] = "SE"
    # check South
    if -1< X_S < int(n_columns) and -1 < Y_S < int(n_rows) and direction == "S" and content[int(X_S)] [int(Y_S)] == "A":
        A_list[X_S, Y_S] = "S"
    # check South West
    if -1< X_SW < int(n_columns) and -1 < Y_SW < int(n_rows) and direction == "SW" and content[int(X_SW)] [int(Y_SW)] == "A":
        A_list[X_SW, Y_SW] = "SW"
    # check West
    if -1< X_W < int(n_columns) and -1 < Y_W < int(n_rows) and direction =="W" and content[int(X_W)] [int(Y_W)] == "A":
        A_list[X_W,Y_W] = "W"

#get count of Ss by the As and following direction
for coordinates , direction in A_list.items():
    X_Y = str(coordinates).split(", ")
    X = X_Y[0].lstrip('(')
    X = int(X)
    Y = X_Y[1].rstrip(')')
    Y = int(Y)
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
#check North
    if -1< X_N < int(n_columns) and -1 < Y_N < int(n_rows) and direction == "N" and content[int(X_N)] [int(Y_N)] == "S":
        count +=1
    #check North East
    if -1< X_NE < int(n_columns) and -1 < Y_NE < int(n_rows) and direction == "NE" and content[int(X_NE)] [int(Y_NE)] == "S":
        count +=1
    #check East
    if -1< X_E < int(n_columns) and -1 < Y_E < int(n_rows) and direction =="E" and content[int(X_E)] [int(Y_E)] == "S":
        count +=1
    # check South East
    if -1< X_SE < int(n_columns) and -1 < Y_SE < int(n_rows) and direction =="SE" and content[int(X_SE)] [int(Y_SE)] == "S":
        count +=1
    # check South
    if -1< X_S < int(n_columns) and -1 < Y_S < int(n_rows) and direction == "S" and content[int(X_S)] [int(Y_S)] == "S":
        count +=1
    # check South West
    if -1< X_SW < int(n_columns) and -1 < Y_SW < int(n_rows) and direction == "SW" and content[int(X_SW)] [int(Y_SW)] == "S":
        count +=1
    # check West
    if -1< X_W < int(n_columns) and -1 < Y_W < int(n_rows) and direction =="W" and content[int(X_W)] [int(Y_W)] == "S":
        count +=1

#print(count)