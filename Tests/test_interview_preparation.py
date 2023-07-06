import json
from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import requests
import unittest


def test_api(self):
    URL = "https://kcentr.ru/content-service/api/desktop/v1/products"
    payload = {
        "visitorUuid": "8485f7ea-f2e7-4478-aff3-e8fe3b0f3cf0",
        "cityUuid": "deb1d05a-71ce-40d1-b726-6ba85d70d58f",
        "categoryId": "televizory",
        "sortType": "price_asc",
        "limit": "19"
    }
    headers = {
        "cookies": "test",
        "callerId": "test_portal"
    }
    response = requests.get(URL, params=payload, headers=headers)
    response_json = response.json()
    response_json_pretty = json.dumps(response_json, indent=4)
    print(response_json_pretty)
    assert response.status_code == 200


def test_lists():
    # Операции със list:
    list_1 = ["banana", 54, "orange", 61]
    # list_1.append("banana")  # добавлява в край
    # list_2 = [33, "apple"]
    # list_1.extend(list_2)  # расширява с друг лист
    # list_1.insert(0, "orange")  # добавлява в конкретен индекс
    # list_1.remove("banana")  # премахва конкретно значение
    # list_1.pop(0)  # премахва конкретен индекс
    # del list_1[0]  # изтрива конкретен индекс
    # list_1.clear() # исчиства лист
    # print(list_1.index("orange")) # печатва номерът на индекса
    # print(list_1.count("orange")) # връща колко елементи имаме с този значение
    # list_1.sort() # сортира в нарастващ ред
    # list_1.reverse() # тази функция обръща нашия списък
    # list_1.copy() # копира нашиат лист
    # for x in list_1:
    #     print(x)
    # for i in range(len(list_1)):
    #     print(list_1[i])
    # i = 0
    # while i < len(list_1):
    #     print(list_1[i])
    #     i = i+1
    # [print(x) for x in list_1]


def test_strings():
    # Операции със String
    a = "Hello, World!"
    b = " Hello, John! "
    # print(a.upper())
    # print(a.lower())
    # print(b.strip()) # Истрива празното пространство
    # print(a.replace("H", "J")) # заменява на друго значение
    # print(a.split(",")) # разделява string а substring
    # ---------------------------------------------------
    # age = 36
    # txt = "My name is John, and I am {}"
    # print(txt.format(age))
    # ---------------------------------------------------
    # quantity = 3
    # itemno = 567
    # price = 49.95
    # myorder = "I want {} pieces of item {} for {} dollars."
    # print(myorder.format(quantity, itemno, price))
    # ---------------------------------------------------
    # quantity = 3
    # itemno = 567
    # price = 49.95
    # myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    # print(myorder.format(quantity, itemno, price))
    # ---------------------------------------------------
    # \n - New Line
    # \' - Single Quote
    # \\ - Backslash
    # \r - Carriage Return
    # \t - Tab
    # \b - Backspace
    # \f - Form Feed
    # \ooo - Octal value print("\110ello World") - Hello World
    # \xhh - Hex value print("\x48ello World") - Hello World
    '''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''
    # ---------------------------------------------------


# Оператори

'''
Operator    Example             Same As

+	        Addition	        x + y	
-	        Subtraction	        x - y	
*	        Multiplication	    x * y	
/	        Division	        x / y	
%	        Modulus	            x % y	
**	        Exponentiation	    x ** y	
//	        Floor division	    x // y

Operator    Example             Same As
=	        x = 5	            x = 5	
+=	        x += 3	            x = x + 3	
-=	        x -= 3	            x = x - 3	
*=	        x *= 3	            x = x * 3	
/=	        x /= 3	            x = x / 3	
%=	        x %= 3	            x = x % 3	
//=	        x //= 3	            x = x // 3	
**=	        x **= 3	            x = x ** 3	
&=	        x &= 3	            x = x & 3	
|=	        x |= 3	            x = x | 3	
^=	        x ^= 3	            x = x ^ 3	
>>=	        x >>= 3	            x = x >> 3	
<<=	        x <<= 3	            x = x << 3


Operator    Name                        Example
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y

x < 5 and  x < 10	
x < 5 or x < 4	
not(x < 5 and x < 10)
x is y
x is not y
x in y
x not in y

'''

# list: a = ["apple", 23, "banana"]
# dictionary: a = {"age": "27", "height": "180"}
# tuple: a = ("apple", 27, "orange")
# set: a = {"apple", 99, "banana"}


'''
Dictionary Methods

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''


def test_open_file():
    file = open("D:/Home PC Part_2/Downloads/Music/reveille-inside-out.mp3")


def test_ui():
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 900)
    URL = "https://www.vanguardmotorsales.com/"
    driver.get(URL)
    time.sleep(2)
    # cart_button = driver.find_element(By.XPATH, "(//a[@title='View Inventory'])[1]")
    cart_button = driver.find_element(By.CSS_SELECTOR, ".vanguard-btn.lg")
    # cart_button.click()
    # time.sleep(2)
    assert cart_button is not None


class Person:
    name = "Ivan"
    age = 20

    def params(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 1


igor = Student()
igor.course = 2
igor.params("Igor", 22)


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Rectangle(Shape, ABC):
    def __int__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        pass

    def perimetr(self):
        pass


# import MySQLdb
# db=MySQLdb.connect(password="moonpie",database="thangs")


def test_lists():
    list_1 = [12, "banana", 99, "apple", 32, 12]
    list_2 = [25, 44, 50, 99, 12, 15]
    list_3 = list_2.sort()
    print(list_1)
    print(list_2)
    print(list_3)


def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


def test_res():
    result = find_max([12, 2, 56, 8, 3])
    print(result)


def test_tt():
    # z = set('abc')
    # z.add('san')
    # z.update(set(['p', 'q']))
    # print(z)
    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7]
    result = l1.append(l2)
    # result = l1 + l2
    print(result)
