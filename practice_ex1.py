''' Write a function called calculate_area that takes base and height as an input and 
    returns and area of a triangle. Equation of an area of a triangle is,
    area = (1/2)*base*height '''

# def calculate_area(height, base):
#     return (1/2)*base*height


# area = calculate_area(10,5)
# print(area)

'''Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape
'''

# def calculate_area(height, base, shape):
#     shape = shape.lower()
#     if shape == 'rectangle':
#         return height*base
#     else:
#         return (1/2)*base*height


# area = calculate_area(10,5, 'Rectangle')
# print('The Area of the given shape is :',area)

'''Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
'''
#  their solutiohn
# def print_pattern(n):
#     for i in range(n):
#         s = ''
#         for j in range(i+1):
#             s = s + '*'
#         print(s)

# My solution

# def print_pattern(n):
#     for i in range(n+1):
#         print('*'*i)

# op = print_pattern(5)


'''
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
'''



# def response(data,userinput):

#     if userinput == 'print':
#         for k,v in data.items():
#             print(k+'==>'+str(v))

#     elif userinput == 'add':
#         con = input('which country you want to add :')
#         if con in data.keys():
#             print('This country exists')
#         else:
#             population = int(input('Please tell the population :'))
#             data[con]=population
#             print(data)

#     elif userinput == 'remove':
#         con = input('which country to remove :')
#         if con in data.keys():
#             data.pop(con)
#             for k,v in data.items():
#                 print(k+'==>'+str(v))
#         else:
#             print('Country does not exist')

#     elif userinput == 'query':
#         con = input('Which country you want to query :')
#         print(f'The population of {con} is', data[con])

#     else:
#         print('Your Response is INVALID, Please Try Again.')


# if __name__== "__main__" :
    
#     data = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}
#     userinput = input('Hi User, Please tell me what would you want to do :')
#     output = response(data, userinput)


'''
You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. 
If stock already exist in your list (like info, ril etc) then it will append the price to the list.
 Otherwise it will create new entry in your dictionary. For example entering 'tata' 
 and 560 will add tata ==> [560] to the dictionary of stocks.
'''

# def operation(stocks, user_input):
#     if user_input == 'print':
#         for i,j in stocks.items():
#             avg = sum(j)/len(j)
#             print(f'{i} ==> {j} ==> avg:  {round(avg, 2)}')

#     elif user_input == 'add':
#         stock_ticker = input('Enter stock ticker :')
#         price = input('Enter stock price :')
#         if stock_ticker in stocks.keys() :
#             stocks[stock_ticker].append(price)
#         else:
#             stocks[stock_ticker] = [price]
            
#     else:
#         print('Unsupported value entered! please try again.')           
  


# if __name__ == '__main__':
    
#     stocks = {
#         'info': [600, 630, 620],
#         'ril' : [1430, 1490, 1567],
#         'mtl' : [234, 180, 160]
#     }

#     user_input = input('Enter the operation :')
#     operation(stocks, user_input)

'''
Write circle_calc() function that takes radius of a circle as an input from user and 
then it calculates and returns area, circumference and diameter. 
You should get these values in your main program by calling circle_calc function and then print them
'''

# def circle_calc(radius):
#     area = 3.14*(radius^2)
#     circumference = 2*3.14*radius
#     diameter = 2*radius

#     return area,circumference,diameter

# if __name__ == '__main__':

#     radius = int(input('Enter the radius of the circle :'))
#     area, circumference, diameter = circle_calc(radius)
#     print(f'Area : {area}, Circumference : {circumference}, diameter : {diameter}')