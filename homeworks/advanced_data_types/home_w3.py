# 1. Define the id of next variables:
int_a = 55
print(id(int_a))
str_b = 'cursor'
print(id(str_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))
# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(5, 4))
# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(5, 4))
# 7. By using keyword arguments into the curly braces.
print("Anna has {0} apples and {m} peaches.".format(5, m="many"))
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {1:5} apples and {0:3} peaches.".format(5, 4))
# 9. With f-strings and variables
clr = "green"
cnt = 5
print(f"Anna has {clr} apples and {cnt} peaches.")
# 10. With % operator
print("Anna has %s apples and %d peaches." % (clr, cnt))
# 11*. With variable substitutions by name (hint: by using dict)
data_dict = {"what clr": clr, 'how much': cnt}
print("Anna has %(what clr)s apples and %(how much)d peaches." % data_dict)

# Comprehensions
# # 12. Convert to list comprehension
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
lst_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
# 13. Convert to regular for with if-else
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
# 14. Convert to dict comprehension.
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
d_comprehension = {x: x ** 2 for x in range(10) if x % 2 == 1}
# 15*. Convert to dict comprehension.
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
d_comprehension1 = {d: d ** 2 if d % 2 == 1 else d // 0.5 for d in range(1, 11)}
# 16. Convert (5) to regular for with if.
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)
# 17*. Convert (6) to regular for with if-else.
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
# 18. Convert to lambda function
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
foo = lambda x, y: x if x < y else y
print(foo(11, 9))
# 19*. Convert to regular function
# foo = lambda x, y, z: z if y < x and x > z else y
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(5, 8, 9))
# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
new_lst = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst)
# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
rsd_lst = list(map(lambda x, y: x ** y, list_A, list_B))
print(rsd_lst)
# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
import functools

lst_sum = functools.reduce(lambda a: a + b, lst_to_sort)
print(lst_sum)
# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_fltr = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_fltr)
# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(- 10, 10)
neg_lst = list(filter(lambda x: x < 0, b))
print(neg_lst)
# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
cmn_lst = list(filter(lambda x: x in list_1, list_2))
print(cmn_lst)
