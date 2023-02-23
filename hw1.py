import data
import math


# Write your functions for each part in the space below.

# Part 1
# Part 1
# Purpose: The program takes in a list of string and returns the number of vowels in that string.
# Input type: a string
# Output type: an int.
def vowel_count(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowel_counter = 0
    for idx in range(len(string)):
        if string[idx].lower() in vowel_list:
            vowel_counter = vowel_counter + 1
    return vowel_counter


#input1 = vowel_count('I am Abdullah a')
#print(input1)


# Part 2
# Purpose: The program takes in a list of ints with len 2 and returns a list with those elements in same order.
# input type: int
# output type: int
# ex. input: [1, 3]
# ex. output: [1, 3]

def short_lists(intgr):
    new_list = []
    for idx in range(len(intgr)):
        length = len(intgr[idx])
        if length == 2:
            new_list.append(intgr[idx])
    return new_list


#input2 = [[8, 5, 3, 2], [1, 2], [6, 8], [9, 7, 5, 3]]
#result = short_lists(input2)
#print(result)


# Part 3
# Purpose: The program would output any nested list that has a length of 2 in accending order and the other lists are the
# same.
# input type: int
# output type: int
# ex input: [[3, 1], [8, 7, 3, 9]]
# ex output: [[1, 3], [8, 7, 3, 9]]

def ascending_pair(intgr):
    new_list = []
    output_list = []
    for idx in range(len(intgr)):
        length = len(intgr[idx])
        if length == 2:
            if intgr[idx][0] > intgr[idx][1]:
                new_list = [intgr[idx][1], intgr[idx][0]]
                output_list.append(new_list)
            else:
                output_list.append(intgr[idx])
        else:
            output_list.append(intgr[idx])

    return output_list


#input3 = [[8, 6], [8, 5, 3, 2], [2, 1], [9, 7, 5, 3]]
#result2 = ascending_pair(input3)
#print(result2)


# Part 4
# Purpose: Given two prices add them and return the answer with cents not going over 99.
# Input type: float
# Output type: float
# Ex input = 20.53+19.99
# Output = 40.52
def add_prices(price_one, price_two):
    sum = price_one + price_two
    return sum


#input4 = add_prices(20.53, 19.99)
#answer = round(input4, 2)
#print(answer)


# Part 5
# Purpose: Given the top left corner and bottom right corner compute the area of the rectangle.
# Input type: float
# Output type: int
# Ex input: Point 1: (1.0, 5.0) Point 2: (4.0, 2.0)
# Output: 9
def rectangle_area(rectangle: [data.Rectangle]):
    width = p2.x - p1.x
    length = p1.y - p2.y
    return length * width


p1 = data.Point(1.0, 5.0)
p2 = data.Point(4.0, 2.0)
r1 = data.Rectangle(p1, p2)

user_input = rectangle_area(r1)
print(user_input)


# Part 6
# Purpose: Given the name of the author of a book it must return the books written by theb author.
# Input type: str
# Output type: str
# Ex input: Neil Gaiman
# Ouput: Good Omens
def books_by_author(author_nme: str, bks: [data.Book]):
    return [book for book in bks if book.authors == author_nme]


# Part 7
# Purpose: Given a rectangle the function must return a circle of that bound from center point to the corner of rectangle.
# Input type: int
# Output type: int
def circle_bound(rectangle: [data.Rectangle]):
    cntr = data.Point((rectangle.top_left.x + rectangle.bottom_right.x) / 2,
                      (rectangle.top_left.y + rectangle.bottom_right.y) / 2)
    dimetr = math.sqrt(
        (rectangle.top_left.x - rectangle.bottom_right.x) ** 2 + (rectangle.top_left.y - rectangle.bottom_right.y) ** 2)
    radius = dimetr / 2
    return data.Circle(cntr, radius)


# Part 8
# Purpose: When given an employees pay it should return all of the employees that are being paid less than the averay pay.
# Input type: int
# Output type: str
def below_pay_average(employee_list: list[data.Employee]):
    if not employee_list:
        return []
    total_payment = sum([employee.pay_rate for employee in employee_list])
    average_payment = total_payment / len(employee_list)
    below_average = [employee.name for employee in employee_list if employee.pay_rate < average_payment]
    return below_average
