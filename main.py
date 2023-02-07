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

s = ''
# hash_tag = '#'
# s = s.replace(' ', '')
# if len(s) < 140 and len(s) != '':
#     print(hash_tag + s)

print(('#' + s.title().replace(' ', ''))\
          if len(s.replace(' ', '')) < 140\
          and s != ''\
          else False)

print('#'*50)
import string
text = 'STDERR'
print(*[string.ascii_lowercase.index(i.lower()) for i in text])

def alphabet_position(text):
    s = [string.ascii_lowercase.index(i.lower()) for i in text]
    z = [int(i+1) for i in s]
    return ' '.join(str(x) for x in z)
def alphabet_position_1(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

def alphabet_position_2(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

print(alphabet_position(text))
print(alphabet_position_1(text))
print(alphabet_position_2(text))

print('#'*50)