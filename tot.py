#created a list by using comprehensive list and the range()
num_list = [num for num in range(1, 11)]
print(num_list)

def sum_num(num_list):
    total = sum(num_list)
    return total

print(sum_num(num_list))

def sum_2(num_list):
    total = 0
    for num in num_list:
        total += num 
    return total

print(sum_2(num_list))
