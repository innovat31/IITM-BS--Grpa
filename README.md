# IITM-BS--Grpa
This repository is for the weekly Graded Programming Assignments of IITM BS Degree.
This is specifically for python Term-2 Jan 2025- April 2025(Term-1 according to the year 2025).

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
