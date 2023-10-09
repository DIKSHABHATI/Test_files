# name = "Diksha Bhati is a Senior Analyst at the Tiger Analytics"
# print(name.split(' ')[::-1])

# def reverse_string(name):
#     return name.split(' ')[::-1]

# name = "Diksha Bhati is a Senior Analyst at the Tiger Analytics"
# result = reverse_string(name)

# print(result)



# def non_rep(li):
#     li = li
#     for i in li:
#         if li.count(i)>1:
#             continue
#         else:
#             print(i)
#             break

# input_string = 'mm name is diksha'
# li = []
# for i in input_string:
#     li.append(i)
# non_rep(li)

# def nrc(name):
#     char_dict = {}
#     for i in name:
#         if i in char_dict:
#             char_dict[i] +=1
#         else:
#             char_dict[i] = 1

#     for j in name:
#         if char_dict[j] == 1:
#             return j 
#     return None


# name = 'my name is yami'
# result = nrc(name)
# print(result)


# str1 = 'diksha'
# # print(sorted(str1))
# str2 = 'shakid'
# # print(sorted(str2))

# def are_anagrams(str1,str2):
#     return sorted(str1) == sorted(str2)

# print(are_anagrams(str1,str2))

# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase to make it case-insensitive
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Check if the lengths of the strings are equal
#     if len(str1) != len(str2):
#         return False

#     # Initialize dictionaries to count character occurrences
#     char_count1 = {}
#     char_count2 = {}

#     # Count character occurrences in str1
#     for char in str1:
#         if char in char_count1:
#             char_count1[char] += 1
#         else:
#             char_count1[char] = 1

#     # Count character occurrences in str2
#     for char in str2:
#         if char in char_count2:
#             char_count2[char] += 1
#         else:
#             char_count2[char] = 1
#     # Compare the dictionaries
#     return char_count1 == char_count2

# # Test cases
# str1 = "listen"
# str2 = "silent"
# print(are_anagrams(str1, str2))  # Output: True

# str3 = "hello"
# str4 = "world"
# print(are_anagrams(str3, str4))  # Output: False

# def find_missing_number(nums, n):
#     expected_sum = n*(n+1)//2
#     actual_sum = sum(nums)
#     return expected_sum-actual_sum

# nums = 1,2,3,5,6,7,9
# n = 9
# results = find_missing_number(nums,n)
# print(results)

# def find_missing_numbers(nums, n):
#     expected_set = set(range(1,n+1))
#     actual_set = set(nums)
#     missing_nums = list(expected_set-actual_set)
#     return missing_nums

# nums = 1,2,3,5,6,7,9
# n = 9
# results = find_missing_numbers(nums,n)
# print(results)

# def merge_intervals(intervals):
#     if not intervals:
#         return []

#     # Sort intervals based on the start point
#     intervals.sort(key=lambda x: x[0])
    
#     merged_intervals = [intervals[0]]
    
#     for interval in intervals[1:]:
#         current_start, current_end = interval
#         previous_start, previous_end = merged_intervals[-1]

#         if current_start <= previous_end:
#             # Overlapping intervals, merge them
#             merged_intervals[-1] = (previous_start, max(current_end, previous_end))
#         else:
#             # Non-overlapping interval, add it to the result
#             merged_intervals.append(interval)

#     return merged_intervals

# intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
# result = merge_intervals(intervals)
# print(result)


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# def generate_fibo_series(n):
#     a,b = 0,1
#     fibo_series = []
#     if n<=0:
#         return fibo_series

#     fibo_series.append(a)
#     if n>1:
#         fibo_series.append(b)

#     for i in range(2,n):
#         next_fibo = a+b
#         fibo_series.append(next_fibo)
#         a,b = b, next_fibo

#     return fibo_series

# n = 5
# op = generate_fibo_series(n)
# print(op)

# def is_palindrome(name):
#     name = name.replace(' ','').lower()
#     return (name == name[::-1])

# out = is_palindrome('rAcecar')
# print(out)

# def is_palindrome(num):
#     num = str(num)

#     start = 0
#     end = len(num)-1

#     while start < end:
#         if num[start] != num[end]:
#             return False

#         start += 1
#         end -= 1

#     return True

# out = is_palindrome('racEAar')
# print(out)



# # Import necessary libraries
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# # Generate synthetic data for demonstration
# np.random.seed(0)
# X = 2 * np.random.rand(100, 1)  # Input feature (1 feature)
# Y = 4 + 3 * X + np.random.randn(100, 1)  # Target variable (with noise)

# # Split the data into training and testing sets
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# # Create a LinearRegression model
# model = LinearRegression()

# # Fit the model to the training data
# model.fit(X_train, Y_train)
# # Make predictions on the test data
# Y_pred = model.predict(X_test)

# # Plot the data and regression line
# plt.scatter(X, Y, label='Data Points')
# plt.plot(X_test, Y_pred, color='red', linewidth=3, label='Linear Regression')
# plt.xlabel('Input Feature (X)')
# plt.ylabel('Target Variable (Y)')
# plt.legend()
# plt.show()

# # Display the model's coefficients and intercept
# print("Intercept (beta0):", model.intercept_[0])
# print("Slope (beta1):", model.coef_[0][0])


# def fibo_series(n):
#     a, b = 0, 1
#     fib_series = []

#     if n <= 0:
#         return fib_series

#     fib_series.append(a)
#     if n > 1:
#         fib_series.append(b)

#     for i in range(2,n):
#         new_fibo = a+b
#         fib_series.append(new_fibo)
#         a , b= b, new_fibo

#     return fib_series

# out = fibo_series(10)
# print(out)

# def reverse_string(name):
#     reversed = ""
#     for char in name:
#         reversed = char + reversed

#     return reversed

# out= reverse_string('diksha')
# print(out)

list1 = [1,2,3,4,4,1,2,2,2,5]

# dic1 = {}

# for i in list1:
#     if i in dic1:
#         dic1[i]+=1

#     else:
#         dic1[i]=1

# print(dic1)

# nw = list1.count(2)
# print(nw)

def is_fib(n):
    a , b = 0, 1
    fib = []

    if n <0:
        return fib
    fib.append(a)
    if n >1:
        fib.append(b)

    for i in range(2,n):
        next_fib = a+b
        fib.append(next_fib)
        a , b = b, next_fib

    return fib

out = is_fib(10)
print(out)