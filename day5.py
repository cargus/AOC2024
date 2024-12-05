def get_rules_with_page (i,page, rules):
    if page[i] in rules:
        return rules[page[i]]
    return False
def check_pages_after_page (check_page, pages_after, string):
    i=0
    x=0
    ref_index = 0
    for numbers in string:
        if numbers == check_page and ref_index  == 0:
            ref_index = numbers[i]
    for pages in pages_after:
        if pages in string:
            check_index =

with open('inputs/day5_input.txt', 'r') as file:
    content = file.read().split("\n\n")
page_order = content[0].splitlines()
update_lists = content[1].splitlines()
rules = {}
i = 0

for rule in page_order:
    line = rule.split("|")
    if line[0] in rules:
        rules[line[0]] = rules[line[0]] + "," + line[1]
    else:
        rules[line[0]] = line[1]
for order in update_lists:
    page = order.split(",")
    n_pages = len(page)
    while i <= n_pages-1:
        test = get_rules_with_page(i,page, rules)
        if test:
            #check all numbers after page[i]
            i+=1
        else:
            break
        print(test)
        # if test: