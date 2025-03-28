# IITM-BS--Grpa
This repository is for the weekly Graded Programming Assignments of IITM BS Degree.
This is specifically for python Term-2 Jan 2025- April 2025(Term-1 according to the year 2025).

* In some cases, multiple solutions are uploaded, all of which are correct.

# Week-1 :

GrPA 1 - Numbers (Arithemetic) - GRADED
Solve the below tasks related to Numbers.

Tasks 1 to 3 - building up Arithemetic expression
Tasks 4 and 5 - floating point arithemetic
Tasks 6 and 7 - modulo and floor division
Problem Type: Input variable - Output Variable, Hidden suffix for evaluation

GrPA2 - Numbers (Relational and Logical) - GRADED
Solve all the below tasks related to relational and logical operators.

This exercise gives you practice in building up boolean expressions.

Problem Type: Input variable - Output Variable, Hidden suffix for evaluation

GrPA 3 - Strings (Indexing and Slicing) - GRADED
Solve all the below tasks related to indexing and slicing.

Keep in mind 🧠 The concept of indexing and slicing will come again in later weeks with list and tuple which are also sequences like string.

This exercise gives you practice in different indexing and slicing methods.

Problem Type: Input variable - Output Variable, Hidden suffix for evaluation

GrPA 4 - Strings (Concatenation, repetition, and substring check) - GRADED
Solve all the below tasks related to string concatenation, repeatition and substring check in strings.

Problem Type: Input variable - Output Variable, Hidden suffix for evaluation

GrPA5 - I/O and Type Conversion - GRADED
Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month, fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number) separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")

Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.

Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".

Note: Finding the tenth_month will be a bit of challange. If you are stuck open the below hint.

Hint for tenth_month
Explanation

When you're adding months to a date, you need to make sure that the month number doesn't go beyond 12, because there are only 12 months in a year.

Starting from Zero:
Think of months like positions on a number line that starts at zero instead of one (because modulo cycles from 0 to n-1). January is 0, February is 1, and so on.
When you subtract 1 from a month, you're basically shifting it to this zero-based system. For example, if you start at month 10 (October), subtracting 1 gives you 9.
Using Modulo:
The modulo operation helps to wrap around when you go past December. So, 13 becomes 1 (January), 14 becomes 2 (February), etc.
The modulo operation works naturally with zero-based numbers. For example, 24 % 12 = 0 means it wraps around to the starting point (January).
Adding 1 Back:
After using the modulo operation, you add 1 back to shift back to the regular month numbering system. This makes sure that months are in the range of 1 to 12.
Example

Let's say it's October (month 10) and you want to find the date 15 months later.

Add the Months:
10 (October) + 15 months = 25.
Convert to Zero-Based and Apply Modulo:
Subtract 1: 25 - 1 = 24.
Apply modulo 12: 24 % 12 = 0.
This means it wraps around to the start of the year.
Convert Back to One-Based:
Add 1: 0 + 1 = 1.
So, it’s January.
Adjust the Year:
Since you added enough months to go into the next year, you need to account for that.
Calculate how many full years you’ve added: (25 - 1) // 12 = 2.
So, if you started in 2022, adding 2 years brings you to 2024.
Result

15 months from October 2022 is January 2024.

Problem Type: Standard Input - Standard Output

# Week-2 :

GrPA 1 - Variables and Assignment - GRADED
Solve all the below tasks related to variables.

This exercise gives you practice in working with variables.

Note: Do not take input or print output as they are taken care by the suffix code(evaluator).

Problem type: Standard Input Standard Output - Input from prefix and Output from suffix

GrPA 2 - String Escaping - GRADED
Assign text that are given in the comments "as is" without the space after the "#" to the corresponding variable names in the template.

Note: There are no inputs to this question, you only have to print the things that are given in the comments in each line

Problem Type - Variable Out - Hidden suffix for input and output

GrPA 3 - Basic conditional patterns - GRADED
This problem gives you exposure to different use cases of if ... elif and else conditional structues.

Part 1 - Only if

Part 2 - if ... else

Part 3 - if ... elif

GrPA 4 - Conditionals - Applications - GRADED
Problem Type: Standard Output - Standard Output

You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.

The operations your application should support are as follows:

Odd number checker: Check whether the input number is odd.
Name: odd_num_check
Inputs: number:int
Output: "yes" if the number is odd, "no" otherwise.
Perfect square checker: Check whether the input number is a perfect square.
Name: perfect_square_check
Inputs: number:int
Output: "yes" if the number is a perfect square, "no" otherwise.
Vowel checker: Check if a string has a vowel in it.
Name: vowel_check
Inputs: text:str
Output: "yes" if the string contains a vowel, "no" otherwise.
Divisibility checker: Check if a number is divisible by 2 or 3.
Name: divisibility_check
Inputs: number:int
Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.
Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
Name: palindrominator
Inputs: text:str
Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)
Simple interest calculator with inputs with a higher interest rate if long term.
Name: simple_interest
Inputs: principal_amount:int, n_years:int (number of years)
Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
If the operation name is not any of the above print "Invalid Operation".

GrPA 5 - Conditionals - Debugging - GRADED
Problem Type: Standard Input - Standard Output, Debugging, and missing

How to solve: To solve this problem use the Python tutor button. Paste the template(buggy) code in the python tutor, you can also include the sample input in the python tutor. This will help you identify the errors easily.

Useful Tips while dealing with indentation

You can indent or detent a line using the keyboard shortcut CTRL+] and CTRL+[ respectively.
To indent or detent a whole block select the block and use the above short cuts.
Useful Keyboard shortcuts for selecting

Use arrow keys to move the cursor in the left, right, up and down directions
Hold Ctrl+ left or right arrow to move the cursor by words
Hold shift key while moving using the above methods to select the contents.
Problem Statement

Write a program to calculate the cost of a meal at a restaurant.

The cost of the meal depends on the main dish and the time of the day.
Main dishes available:
"paneer tikka": ₹250
"butter chicken": ₹240
"masala dosa": ₹200
Additional discounts:
15% discount for meals ordered during lunchtime (from 12 PM to 3 PM).
Customers can apply vouchers for an additional 10% discount on the total cost.
The restaurant accepts card payments.
For card payments, there's an additional service charge of 5% on the total cost after applying any discounts.
Take the following inputs:
Main dish : str
Time of the day: int: 24-hour format
Whether the customer has a voucher: bool: True/False
Whether the payment is by card: bool: True/False
Calculate and display the total cost of the meal.

# Week-3 :
 
GrPA 1 - While Loop - GRADED
✅ Important Note on while loop🔁:

Use while only when the number of iterations is indefinite.
If you can term the steps as do n times, do once for each item, etc. use for loop instead.
If you can only term the steps as do until something happens. Like when user inputs 10.
A bit of wisdom 📖 There are maily two ways in which while loops are used in the context of taking inputs until a terminal word.

Method 1
Method 2
# method 1
a = input()
while a != terminal_word: # opposite of the terminal condition
    # do something with a
    a = input() # take the next a

# method 2
while True: # loop forever
    a = input()
    if a == terminal_word: # the terminal condition
        break
    # do something with a
Problem Statement

Problem type - Standard Input - Standard Output

NOTE: None of this problem statements can be written using a for since the number of repetition is indefinite.

Implement different parts of a multi-functional program based on an initial input value. Each part of the program will handle various tasks related to accumulation, filtering, mapping, and combinations of these operations. None of the tasks should use explicit loops for definite repetitions, and the program should handle indefinite inputs gracefully.

Tasks

Accumulation - Accumulating a final result
sum_until_0: Continuously read integers from standard input until you receive a zero. Print the sum of these integers.
total_price: Continuously read pairs of integers from standard input, representing the quantity and price of items, until you receive the string "END". Print the total price of all items.
Filtering - Selecting based on a criterion
only_ed_or_ing: Continuously read strings from standard input until you encounter the word "STOP" (case insensitive and not included in the output). Print only those strings that end with "ed" or "ing" (case insensitive).
reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output). Print only those integers for which the sum of the number and its reverse is a palindrome.
Mapping - Applying the same operation to different items
double_string: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.
odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output). Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.
Filter and Map - Applying an operation to selected items
only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. Print the square of each number only if it is even.
Filter and Accumulate - Accumulating a result with selected items
only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.

GrPA 2 - For Loop - GRADED
Bit of Wisdom 📖 In context of general incremental definite loops the structure of while loop can be converted to a for loop using range. Refer this.

# the wile loop
i = 0 # initialization
while i<10: # condition
    print(i) # body
    i+=2 # update

# same with for loop
for i in range(0,10,2): # range combines initalization, temination and update.
    print(i)
Write a multi functional program that takes input task from standard input and does the corresponding taks accordingly. Note that the useage of for loop is not allowed in this exercise.

Part 1 - while loop to for loop
factorial - print factorial of a given non-negative integer n (Type: Accumulation)
Input - n:int
even_numbers - Print the even numbers from 0 (including) till the given input number n(including) in multiple lines (Type: Just Iterating)
Input - n:int
power_sequence - Print the sequence 1, 2, 4, 8, 16, ... n terms in same line in multiple lines, where n is taken from the input(Type: Mapping)
Input - n:int
Part 2 - for loop With range
sum_not_divisible - Print the sum of positive less that the given number n and not divisible by 4 and 5. (Type: Filtered Accumulation)
Input - n:int
from_k - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k which do not have the digit 5 and 9 and is odd number in multiple lines.
Input - n:int, k:int
part 3 - for loop with iterables.
string_iter - Given a string s of digits print the numerical value of the digit multiplied by the previous digit. Assume the pevious digit for the first element to be 1.
Input - s:str
list_iter - Print the elements of a list l line by line in the format {element} - type: {type} where the element is the current element being iterated by the for loop and type is the type of the element. (Even though list are not covered in this week, this is included to demonstrate the similarity between iterating characters in a str and items in a list)
Input - l:list

GrPA 3 - Nested loops - GRADED
Create a multi-functional program that performs different tasks based on the user input. The program should support the following tasks:

Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.
Sorted Permutation (sorted_permutation): Given a string s, print all the possible two-letter permutations(without repetition) of the letters in the string where the first character comes before the second one in alphabetical order. The order in which the permutations are printed is same as the previous one (Type: Filtering).
Repeat the Repeat (repeat_the_repeat): Given a number n, print the numbers from 1 to n in the same line and repeat this n times.
Repeat Incrementally (repeat_incrementally): Given a number n, print a pattern where the k-th line contains the first k numbers and there are n lines in total. For example, if n is 4, the output should be:
1
12
123
1234
Increment and Decrement (increment_and_decrement): Given a number n, print a pattern where the k-th line should have the numbers from 1 to k and then back down to 1. For example, if n is 4, the output should be:
1
121
12321
1234321

GrPA 4 - Loops Application - GRADED
You are tasked with writing a program that can handle various tasks based on the input. The first line of the input represents the task to be performed. The possible tasks are:

factors - Find the factors of a number n (including 1 and itself) in ascending order.
find_min - Take n numbers from the input and print the minimum number.
prime_check - Check whether a given number is prime or not.
is_sorted - Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.
any_true - Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.
manhattan - Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.
Write a program to solve these tasks. Use loops where necessary.

# Week-4 :

GrPA 1 - Basic Collections 
A bit of wisdom 📖

Iterable - Something that can be used in a for loop.
Collection - Datatypes that hold many values like list, set, tuple and dict.
All iterables are not collections. Eg. str and range are iterables but not collections.
All collections are iterables.
Only ordered collections are indexable and slicable
Only Mutable collections can be modified
Hasing is a method used in collections like set to check whether an element is present or not quickly, and in dict to retrive the value for the given key quickly. There are only certain datatypes that can be hashed. For example
## Sample Table

## Python Data Types Table

| Data Type | Iterable | Collection | Indexable / Slicable | Ordered | Mutable | Uses Hashing |
|-----------|----------|------------|----------------------|---------|---------|--------------|
| **str**   | ✅       | ❌         | ✅                   | ✅      | ❌      | ❌           |
| **range** | ✅       | ❌         | ❌                   | ✅      | ❌      | ❌           |
| **list**  | ✅       | ✅         | ✅                   | ✅      | ✅      | ❌           |
| **tuple** | ✅       | ✅         | ✅                   | ✅      | ❌      | ❌           |
| **set**   | ✅       | ✅         | ❌                   | ❌      | ✅      | ✅           |
| **dict**  | ✅       | ✅         | ❌                   | ❌      | ✅      | ✅ (on keys) |


built-in functions - some functions like sum, min, max, sorted, reversed will help in doing some basic tasks.
Any iterable can be converted into a list or a tuple
Any iterable of hashable data types can be converted into a set
Learning objectives

NOTE In this exercise we will not be using dict as they will be introduced in next week.

Empty collections
Singleton Collections
True-ness and False-ness in collections
Inbuilt functions for collections
Indexing and Slicing
Membership checks
Concatenation

Problem Type: Input variable - Output Variable, Hidden suffix for evaluation

Instructions on how to solve (Click to expand)
NOTE: In this type of questions you should not take input or print anything unless your are explicitly asked to. Assign the result of the required computation to the correct variable name as it will be evaluated for type and value by the evaluator.

The input variables will be assigned by the evaluator based on the test cases.

The grey part before the white part (if any) in the code is the prefix code. The grey part after the white part (if any) is the suffix code which are not editable. Usually they will be the part of code but in this type of questions it will be removed by the evaluator.

The Three dots (...) called as Ellipsis in python are like placeholders, replace them with your answer.

The inputs on the code blocks are just sample inputs they won't be evaluated in the actual testcases.

Each testcase will have its own set of testcases defined as variables. The check function in the testcases is in the hidden evaluation code that checks the value and type of the variable.

Template Code(Click to Expand)
empty_list = ... 
empty_set = ... # be carefull here you might end up creating something called as an empty dict 
empty_tuple = ... 

singleton_list = ... # list: A list with only one element
singleton_set = ... # set: A set with only one element
singleton_tuple = ... # tuple: A tuple with only one element

a_falsy_list = ... # list: a list but when passed to bool function should return False.
a_falsy_set = ... # set: a list but when passed to bool function should return False.
a_truthy_tuple = ... # tuple: a tuple but when passed to bool function should return True

int_iterable_min = ... # int: find the minimum of int_iterable. Hint: use min function
int_iterable_max = ... # int: find the maximum of int_iterable. Hint: use max function
int_iterable_sum = ... # int: you know what to do
int_iterable_len = ... # int: really... you need hint?
int_iterable_sorted = ... # list: the int_iterable sorted in ascending order
int_iterable_sorted_desc = ... # list: the int_iterable sorted in desc order

if ... : # some iterables are not reversible why?
    int_iterable_reversed = ... # list: the int_iterable reversed use the reversed function
else: # in that case sort it in ascending order and reverse it
    int_iterable_reversed = ... #list

if ...: # some collections are not indexable why?
    third_last_element = ... # the third last element of `some_collection`
else: # in that case set third_last_element to None
    third_last_element = ... 

if ...: # some collections are not slicable
    odd_index_elements = ... # type(some_collection): the elements at odd indices of `some_collection` 
else: # in that case set odd_index_elements to None
    odd_index_elements = ... 

is_some_value_in_some_collection = ... # bool: True if `some_value` is present in `some_collection`

if ...: # some collections are not ordered
    is_some_value_in_even_indices = ... # bool: True if `some_value` is present in even indices of `some_collection`
else: # in that case set is_some_value_in_even_indices to None
    is_some_value_in_even_indices = ...

all_iterables = ... # list: concatenate `some_iterable`, `another_iterable` and `yet_another_iterable` into a list.

if ... : # some iterables are not ordered
    all_concat = ... # str: concatenate all the strings in string_iterable with '-' in between
else: # in that case sort them and concatenate
    all_concat = ...

GrPA 2 - Operations on list and set 
List mutating operations - This will help you learn the list methods and operations that will modify the list inplace. Note that you should not be creating a new list anywhere in this function.
Create new lists - This will help you learn how to create new lists that resembles the result of above operations but does not affecting the original list.
Set operations - This will help you learn things that you can do with sets.    

GrPA 3 - List and set application 
Implement the following functions:

find_min: Find the minimum value in a list of integers.
Input: A list of integers.
Output: An integer, the minimum value in the list.
odd_increment_even_decrement_no_modify: Increment all the odd numbers in a list by 1 and decrement all the even numbers by 1, without modifying the original list.
Input: A list of integers.
Output: A new list of integers with the modified values.
odd_square_even_double_modify: Square all the odd numbers and double all the even numbers in a list, modifying the list in place.
Input: A list of integers.
Output: None (the input list is modified in place).
more_than_two_unique_vowels: Given a string of comma-separated words, return a set containing words that have more than two unique vowels.
Input: A string of comma-separated words.
Output: A set of words with more than two unique vowels.
sum_of_list_of_lists: Given a list of lists of integers, find the sum of all the integers in all the lists.
Input: A list of lists of integers.
Output: An integer, the sum of all the integers in the nested lists.
flatten: Flatten a list of lists into a single list.
Input: A list of lists.
Output: A single flattened list.
all_common: Find the common characters that are present in all strings in a list of strings and return them as a string in ascending order.
Input: A list of strings.
Output: A string containing common characters in ascending order.
vocabulary: Given a list of sentences (with only alphabets and spaces), find the vocabulary (list of unique words) and return it as a set. Convert all words to lowercase before adding to the vocabulary.
Input: A list of sentences.
Output: A set of unique words in lowercase.

GrPA 4 - Function Basics 
You are required to complete the following functions to perform various operations on tuples and lists.

swap_halves: Swap the first and second halves of a tuple with an even length.
Input: A tuple of even length.
Output: A new tuple where the first and second halves are swapped.
swap_at_index: Break a tuple at a given index ( k ) (the element at the ( k )-th index is included in the first half before swapping) and swap the parts.
Input: A tuple and an integer ( k ).
Output: A new tuple where the parts before and after the ( k )-th index are swapped.
rotate_k: Create a new list with elements of the given list moved ( k ) positions towards the right. The elements at the end should come back to the beginning in a circular order.
Input: A list and an integer ( k ) (default value ( k = 1 )).
Output: A new list with the elements rotated ( k ) positions to the right.
first_and_last_index: Get the indices of the first and last occurrence of a given item in a list. Assume the item is present in the list at least once.
Input: A list and an item.
Output: A tuple with the first and last indices of the given item in the list.
reverse_first_and_last_halves: Reverse the first and last halves of a list with even length in place.
Input: A list with an even length.
Output: None (the list should be modified in place).

GrPA 5 - Comprehensions 
This will help you build up the basics of list comprehensions.

sum_of_squares - find the sum of squares of numbers in a list - (mapping and aggregation)
total_cost - given quantitiy and price of each item as a list of tuples find the total cost using list comprehensions
abbreviation - given a string with multiple words seperated by space, form an abbrevation out of it by taking the first letter in caps. (mapping and aggregation)
palindromes - given a list of strings, create a new list with only palindromes filtering
all_chars_from_big_words - find the all unique characters (case insensitive, make all lowercase) from all words with size greater than 5 in a given sentence with words seperated by spaces. (filtering)
flatten - flatten a nested list using comprehension
unflatten - given a flat list and number of rows, create a matrix (2d list) with that number of rows. (nested-aggregation)
make_identity_matrix - make an identity (with ones on the main diagonal and zeros elsewhere) given the size.
make_lower_triangular_matrix - given number of rows m, create a lower triangular matrix like the pattern below. for m = 5
[
  [1,0,0,0,0],
  [1,2,0,0,0],
  [1,2,3,0,0],
  [1,2,3,4,0],
  [1,2,3,4,5]
]
Note: you cannot use if statements or loops withing the functions.

# Week - 5 :

GrPA 1 - Dictionary Basics - GRADED
You are tasked with implementing a series of functions that perform various operations on dictionaries in Python. These functions will manipulate dictionaries that represent fruit prices and perform different operations as specified.

dictionary_operations(fruit_prices: dict, fruits: list)

Perform a series of operations on the given fruit_prices dictionary based on the fruits list:

Add fruits[0] with a cost of 3.
Modify the cost of fruits[1] to 2.
Increase the cost of fruits[2] by 2.
Delete fruits[3] from fruit_prices.
Print the price of fruits[4].
Print the names of fruits in fruit_prices as a sorted list.
Print the prices of fruits in fruit_prices as a sorted list.
increase_prices(fruit_prices: dict) -> None

Increase the prices of every fruit by 20% and round to two decimal places. Modify the dictionary in place.

dict_from_string(string: str, key_type, value_type)

Convert a string with comma-separated key-value pairs into a dictionary, converting the keys and values to the specified types.

dict_to_string(D: dict) -> str

Convert a dictionary back into a string with each key-value pair on a new line, using comprehensions.

GrPA 2 - Dictionary Applications - GRADED
Implement the below functions as per the docstrings.

def total_price(fruit_prices: dict, purchases) -> float:
    '''
    Compute the fruit prices give the quantity of each fruit. Do not use the sum function.

    Arguments:
    fruit_prices: dict - fruit name as key and price as value
    purchases: list[tuple] - as list of tuples of (fruit, quantity)

    Return:
    total_price: float
    '''
    ...

def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    '''
    Compute the total price without loops.
    '''
    ...

def find_cheapest_fruit(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit from the fruit_prices dict, do not use min function

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    cheapest_fruit: str - the fruit with the lowest price
    '''
    ...

def find_cheapest_fruit_no_loops(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit using min function. Do not use loops
    '''
    ...

# grouping
def group_fruits(fruits:list):
    '''
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.

    Arguments:
    fruits - list: list of fruit names

    Return:
    dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.
    '''
    ...

# binning
def bin_fruits(fruit_prices):
    '''
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    '''
    ...

    GrPA 3 - Composing functions - GRADED
Implement all the given functions that are used to solve the below problems.

Follow the path

You are given a matrix of size m x n consisting of ones (1) and zeros (0). There is a single continuous path formed with ones that starts from the rightmost cell in the last row (m-th row) with one and ends at leftmost cell in the first row with one in it. The path does not branch, and there is only one such path. Your task is to traverse along the path and print the coordinates of the path from start to end as tuples over multiple lines. The path can move vertically and horizontally.

Input

matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
Output

(4,1)
(4,0)
(3,0)
(2,0)
(2,1)
(2,2)
(2,3)
(1,3)
(0,3)
(0,2)
Alternate the path Same setup, but while going in that path, flip every ones in the even position in the path to 2. Modify the matrix inplace.

Output

[
    [0, 0, 2, 1],
    [0, 0, 0, 2],
    [2, 1, 2, 1],
    [1, 0, 0, 0],
    [2, 1, 0, 0]
]
Count the path Same setup, but instead of flipping put the count of the step in the path. Modify the matrix inplace.

Output

[
    [0, 0, 10, 9],
    [0, 0, 0, 8],
    [4, 5, 6, 7],
    [3, 0, 0, 0],
    [2, 1, 0, 0]
]
Mirror the path horizontally Same setup, but also add a path that is the horizontal mirror of the original path in the same matrix.

Input

[
  [0,1,0,0,0],
  [0,1,1,1,0],
  [0,0,0,1,0],
  [0,0,0,1,1]
]
Output

[
  [0,1,0,1,0],
  [0,1,1,1,0],
  [0,1,0,1,0],
  [1,1,0,1,1]
]
Mirror the path vertically Same setup, but also add a path that is the vertical mirror of the original path in the same matrix.

Input

[
  [0,1,0,0,0],
  [0,1,1,1,0],
  [0,0,0,1,0],
  [0,0,0,1,1]
]
Output

[
  [0,1,0,1,1],
  [0,1,1,1,0],
  [0,1,1,1,0],
  [0,1,0,1,1]
]

GrPA 4 - lambda, zip, enumerate, map, filter - GRADED
Implement the given functions according to the docstrings.

# mapping
def is_greater_than_5(numbers:list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''
    ...

# filtering
def filter_less_than_5(numbers:list)->list:
    '''Given an list of numbers, return a list of numbers that are less than 5'''
    ...

# aggregation with filtering
def sum_of_two_digit_numbers(numbers:list):
    '''Given a list of numbers find the sum of all two_digit_numbers.
    '''
    ...

# aggregation with mapping
def is_all_has_a(words:list)->bool:
    '''Given a list of words check if all words has the letter a(case insensitive) in it.
    '''
    ...

# enumerate
def print_with_numbering(items): 
    '''
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    '''
    ...

# zip
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    '''
    ...

# key value list to dict
def make_dict(keys, values):
    '''Create a dict with keys and values'''
    ...

# enumerate with filtering and map
def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of the big words(length greater than 5).
    '''
    ...

# zip with mapping and aggregation
def decode_rle(chars:str, repeats:list)->str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times. 

    Note rle refers to Run-length encoding
    '''
    ...

    GrPA 5 - min, max, sorted, groupby - GRADED
Implement all the given functions below according to the docstring.

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''
    ...

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''
    ...

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    ...

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    ...

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    ...

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    ...

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    ...

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    ...

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''
    ...

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    ...

 # Week-6 :

Numbers 1 :
Find percentage increased
Write a function to calculate the percentage increase from the original value to the new value.

Assume original is less than or equal to new.

Examples

>>> percentage_increased(50, 75)
50.0
>>> percentage_increased(80, 100)
25.0

def percentage_increased(original, new):
    '''Calculate the percentage increase from the original value to the new value.

    Assume original is less than or equal to new.

    Args:
        original (float): The original value.
        new (float): The new value.

    Returns:
        float: The percentage increase.

    Examples:
    >>> percentage_increased(50, 75)
    50.0
    >>> percentage_increased(80, 100)
    25.0
    '''
    ...

 Numbers 2 :

Check if ten digit even number
Write a function to check if a number is a ten-digit even number.

Also account for negative numbers discarding the sign.

Examples

>>> is_ten_digit_even(8769473839)
False
>>> is_ten_digit_even(928948)
False
>>> is_ten_digit_even(9289479278)
True
>>> is_ten_digit_even(-9289479278)
True

def is_ten_digit_even(n):
    '''Checks if a number is a 10 digit even number.

    Also account for negative numbers discarding the sign.

    Args: 
        n (int): The given number. 
    
    Returns: 
        bool : result as True or False. 
    
    Examples:
    >>> is_ten_digit_even(8769473839)
    False
    >>> is_ten_digit_even(928948)
    False
    >>> is_ten_digit_even(9289479278)
    True
    >>> is_ten_digit_even(-9289479278)
    True
    '''
    ...

Numbers 3 :

Arithmetic Operations tuple from two integers
Given a tuple of two integers (a, b), return a tuple containing the sum, difference, product, and quotient (integer division) of the two numbers.

Example:

>>> arithmetic_operations((1, 2))
(3, -1, 2, 0)

def arithmetic_operations(t: tuple) -> tuple:
    '''
    Given a tuple of two integers (a, b), return a tuple containing the 
    sum, difference, product, and quotient (integer division) of the two numbers.

    Arguments:
    t: tuple - a tuple of two integers (a, b)

    Return:
    tuple - a tuple containing the sum, difference, product, and quotient

    Example:
    >>> arithmetic_operations((1, 2))
    (3, -1, 2, 0)
    '''
    ...

Strings-1 :
Format Elements in tuple as "second, first"
Given a tuple of length two create a string in the format of "second, first" where first and second are the first and second elements in the tuple.

The elements can be of any data type.

Example

>>> format_as_second_comma_first(('hello', 'python'))
'python, hello'
>>> format_as_second_comma_first((1, 2))
'2, 1'

def format_as_second_comma_first(t: tuple) -> str:
    '''Formats the two elements in a tuple as "second, first".

    Arguments:
    t: tuple - a tuple two elements

    Return:
    str - a formatted string "second, first"

    Example:
    >>> format_as_second_comma_first(('hello', 'python'))
    'python, hello'
    >>> format_as_second_comma_first((1, 2))
    '2, 1'
    '''
    ...

Strings-2 :
Even Characters first and Odd Characters reversed
Given a string, return a string with the characters in the even indices first and the characters in the odd indices next but in reversed order.

Example For the input "abcde",

even chars = "ace"
odd chars = "bd"; odd chars reversed = "db"
result = "acedb"

def even_first_odd_reversed(s: str) -> str:
    '''Return a string with the characters in the even indices first 
    and the characters in the odd indices reversed next.

    Arguments:
    s: str - the input string

    Return:
    str - modified string

    Example:
    >>> even_first_odd_reversed('abcde')
    'acedb'
    >>> even_first_odd_reversed('python')
    'ptonhy'
    '''
    ...

Strings-3 :
Palindrome Integer
Given an integer, check whether it is a palindrome. A palindrome is a number or a string that reads the same backward as forward.

Assume the numbers are positive.

Example

is_palindrome(121) == True
is_palindrome(123) == False
is_palindrome(1212) == False
Template Code(Click to Expand)

def is_palindrome(n: int) -> bool:
    '''Checks if an integer is a palindrome.

    Arguments:
    n: int - the integer to check

    Return:
    bool - True if the integer is a palindrome, False otherwise
    '''
    ...

Collections-1 :
