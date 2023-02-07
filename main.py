############### task 1

a = [1, 2, 2]
b = [2]
########## var 1
# # print([a.remove(x) for x in a for x in a if x in b])
# # print(a)
######## var 2
print([x for x in a if x not in b])

for x in a:
    if x not in b:
        print(x)


############## task 2

# text_str = 'asdgaaast sdufisdfgaeg'
# ########### var 1
#
# count = 0
# vowels = ['a', 'e', 'i', 'o', 'u']
# for symbol in text_str:
#     if symbol in vowels:
#         count += 1
# print(count)
# ############ var 2
#
# print(sum(1 for i in text_str if i in 'aeiouAEIOU'))
def min_num(num):
    c = 1000
    for i in num:
        if c > int(i):
            c = int(i)
    return c


def max_num(num):
    c = -1000
    for i in num:
        if c < int(i):
            c = int(i)
    return c


numbers = "305 592 -700 -635 249 -283 689 -130 537 911 475 738 85 809 886"
x = numbers.split()
print(x)
max_x = max(x)
print(max_x)
min_x = min_num(x)
print(min_x)
numbers = str(max_x) + ' ' + str(min_x)
print(numbers)
