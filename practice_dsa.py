# numbers = [1, 4, 67, 43, 12, 68, 7, 98, 5]
# # search for number = 68

# # for i in range(len(list)):
# #     if list[i] == 68:
# #         print(i)
        
# sorted_list = sorted(numbers)
# mid = len(sorted_list)//2
# print(sorted_list[mid])
# if sorted_list[mid] <68:
#     next_li = sorted_list[mid:]
#     mid_1 = len(next_li)//2
#     if next_li[mid_1] <68:
#         next_li1 = next_li[mid_1:]
#         mid_2 = len(next_li1)//2
#         if mid_2 == 68:
#             return numbers.index(68)

expense = [2200, 2350, 2600, 2130, 2190]

print(f"Feb had INR {expense[1]-expense[0]} more expenses than Jan")
print(f"The total expense is INR {expense[0]+expense[1]+expense[2]} in first three months of the year")

if 2000 in expense:
    print('Yes, INR 2000 is in the expenses list')
else:
    print('No, there is not any expense of INR 2000')

expense.append(1980)
expense[4] = expense[4]-200
print('The Updated expense for April month is', expense[4])






# print(mid)
# print(sorted_list[mid])

# for i in range(4, len(sorted_list)-1):
#     if sorted_list[i] == 68:
#         print(i)