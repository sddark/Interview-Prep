### If ... Else
---

Python supports the usual logical conditions from mathematics:

Equals: a == b

Not Equals: a != b

Less than: a < b

Less than or equal to: a <= b

Greater than: a > b

Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

If statement:

`a = 33`

`b = 200`

`if b > a:`

` > print("b is greater than a")`

In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

The else keyword catches anything which isn't caught by the preceding conditions.

If you have only one statement to execute, you can put it on the same line as the if statement.

`if a > b: print("a is greater than b")`

The and keyword is a logical operator, and is used to combine conditional statements

`a = 200`

`b = 33`

`c = 500`

`if a > b and c > a:`

`>  print("Both conditions are True")`

The or keyword is a logical operator, and is used to combine conditional statements:

`a = 200`

`b = 33`

`c = 500`

`if a > b or c > a:`

`>  print("At least one of the conditions is True")`

You can have if statements inside if statements, this is called nested if statements.

if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

`a = 33`

`b = 200`

`if b > a:`

`>  pass`

### While Loops
---
With the while loop we can execute a set of statements as long as a condition is true.

Print i as long as i is less than 6:

`i = 1`

`while i < 6:`

`>  print(i)`

`>  i += 1`

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

With the break statement we can stop the loop even if the while condition is true

With the continue statement we can stop the current iteration, and continue with the next

With the else statement we can run a block of code once when the condition no longer is true:

`i = 1`

`while i < 6:`

`>  print(i)`

`>  i += 1`

`else:`

`>  print("i is no longer less than 6")`

### For Loop
---
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

`fruits = ["apple", "banana", "cherry"]`

`for x in fruits:`

`>  print(x)`

The for loop does not require an indexing variable to set beforehand.

Even strings are iterable objects, they contain a sequence of characters:

With the break statement we can stop the loop before it has looped through all the items:

`fruits = ["apple", "banana", "cherry"]`

`for x in fruits:`

`>  print(x)`

`>  if x == "banana":`

`> >   break`

With the continue statement we can stop the current iteration of the loop, and continue with the next

To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

`for x in range(6):`

`>  print(x)`

The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`:

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

Note: The else block will NOT be executed if the loop is stopped by a break statement.

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop"

for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

### Match Case
---
Match case is implemented to evaluate expressions against multiple values.

# First, ask the player about their CPU
cpuModel = str.lower(input("Please enter your CPU model: "))
 
The match statement evaluates the variable's value

`match cpuModel:`

`case "celeron": # We test for different values and print different messages`

`        print ("Forget about it and play Minesweeper instead...")`

`case "core i3":`

`        print ("Good luck with that ;)")`

`case "core i5":`

`        print ("Yeah, you should be fine.")`

`case "core i7":`

`        print ("Have fun!")`

`case "core i9":`

`        print ("Our team designed nice loading screens… Too bad you won't see them...")`

`case _: # the underscore character is used as a catch-all.`

`        print ("Is that even a thing?")`