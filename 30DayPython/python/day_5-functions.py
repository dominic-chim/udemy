items = ["Mic","Phone",323.12,3123.123,"Justin","Bag","Cliff Bars",134]
str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass

print(str_items)

print(num_items)


def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items

print(parse_lists(items))

new_num_list = ["a",1,343,"bssd",555.34,"asdw","test",65]
def my_sum(num_list):
    total =0
    num_count = 0
    for i in num_list:
        if isinstance(i, float) or isinstance(i, int):
            total+=i
            num_count+=1
        else:
            pass
    return total,num_count

def my_avg(some_list):
    total, num_of_items = my_sum(some_list)
    return total/ (num_of_items * 1.0)
print(my_avg(new_num_list))