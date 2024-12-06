# create a dictionary of the first number as the key and a list of all of the second numbers associated with it
def make_rules_dict(page_order_list: list) -> dict[int:list[int]]:
    rules_dict: dict[int:list[int]] = {}
    for rule in page_order_list:
        line = rule.split("|")
        if int(line[0]) in rules_dict:
            rules_dict[int(line[0])] += [int(line[1])]
        else:
            rules_dict[int(line[0])] = [int(line[1])]
    return rules_dict


# logic to check page numbers against rules list
def check_all_pages_in_order(pages_to_check, rules_to_follow):
    for i in range(len(pages_to_check) - 1):
        current_page = int(pages_to_check[i])
        if current_page in rules_to_follow:
            test_numbers = rules_to_follow[current_page]
            test_pages = pages_to_check[i + 1:]
            for x in range(len(test_pages)):
                if int(test_pages[x]) not in test_numbers:
                    wrong_lists.append(pages_to_check)
                    wrong_index.append(x)
                    return 0
        else:
            wrong_lists.append(pages_to_check)
            return 0
    return get_center_number(pages_to_check)


# find center number of list
def get_center_number(number_list):
    center = int(len(number_list) / 2)
    value = number_list[center]
    return int(value)


def get_page_out_of_order(pages_to_check, rules_to_follow):
    for i in range(len(pages_to_check)):
        current_page = int(pages_to_check[i])
        if current_page in rules_to_follow:
            test_numbers = rules_to_follow[current_page]
            test_pages = pages_to_check[i + 1:]
            for x in range(len(test_pages)):
                if int(test_pages[x]) not in test_numbers:
                    return x
        else:
            return i
    return len(pages_to_check)


def move_number_to_fix(line_to_fix):
    try:
        return line_to_fix[1:] + [line_to_fix[0]]
    except:
        return line_to_fix


def fix_line_order(line_to_fix : list[int], rules: dict[int:[list[int]]]) -> list[int]:
    if not line_to_fix:
        return []
    if len(line_to_fix)==1:
        return line_to_fix
    broken_index = get_page_out_of_order(line_to_fix, rules)
    fixed_list = line_to_fix[0:broken_index]
    line_to_fix = move_number_to_fix(line_to_fix[broken_index:])
    return fixed_list + fix_line_order(line_to_fix, rules)



# open file and split by number pairs and number lists off empty line
with open('inputs/day5_input.txt', 'r') as file:
    content = file.read().split("\n\n")

# assign number pairs and number lists unique variables and split into lists by lines
page_order_rules = content[0].splitlines()
update_lists = content[1].splitlines()

# define global variables
i = 0
x = 0
total = 0
wrong_lists = []
wrong_index = []
total_2 = 0
# make a dictionary of all the rules for each page
rules = make_rules_dict(page_order_rules)

for order in update_lists:
    page = order.split(",")
    test = check_all_pages_in_order(page, rules)
    total += test
print("part 1 answer is " + str(total))

for index in range(len(wrong_lists)):
    wrong_list = wrong_lists[index]
    new_line = fix_line_order(wrong_list, rules)
    total_2 += get_center_number(new_line)
print("part 2 answer is " + str(total_2))
