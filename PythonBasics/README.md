# Python Basic Langauge
Variables can store data of different types, and different types can do different things.
### Python Data Types
---
Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview

None Type:	NoneType

You can get the data type of any object by using the `type()` function:

### Setting Data Type
---
 Example | Data Type 
 ---|---
x = "Hello World" | str	
x = 20 | int	
x = 20.5 | float	
x = 1j | complex	
x = ["apple", "banana", "cherry"] | list	
x = ("apple", "banana", "cherry") | tuple	
x = range(6) | range	
x = {"name" : "John", "age" : 36} | dict	
x = {"apple", "banana", "cherry"} | set	
x = frozenset({"apple", "banana", "cherry"}) | frozenset	
x = True | bool	
x = b"Hello" | bytes	
x = bytearray(5) | bytearray	
x = memoryview(bytes(5)) | memoryview	
x = None | NoneType | 

### Casting
---
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

`int()` - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

`float()` - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

`str()` - constructs a string from a wide variety of data types, including strings, integer literals and float literals

`x = int(1)` # x will be 1

`x = float(1)` # x will be 1.0

`x = str("s1")` # x will be 's1'

### Strings
---
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

`print("Hello")`

You can assign a multiline string to a variable by using three quotes:

`a = """Lorem ipsum dolor sit amet,`

`consectetur adipiscing elit.""" `

or three single quotes

`a = '''Sed do eiusmod tempor incididunt`

`ut labore et dolore magna aliqua.'''`

Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

`a = "Hello, World!"`

`print(a[1]) # H`

String Length

To get the length of a string, use the len() function.

`a = "Hello, World!"`

`print(len(a))`

Check String

To check if a certain phrase or character is present in a string, we can use the keyword in.

`txt = "The best things in life are free!"`

`print("free" in txt) # True`

Check if NOT

To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

`txt = "The best things in life are free!"`

`print("expensive" not in txt) # False`

Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Get the characters from position 2 to position 5 (does not include 5th element):

`b = "Hello, World!"`

`print(b[2:5]) # llo`

Get the characters from the start to position 5 (does not include 5th element):

`b = "Hello, World!"`

`print(b[:5]) # Hello`

Get the characters from position 2, and all the way to the end (includes 2nd element):

`b = "Hello, World!"`

`print(b[2:]) # llo, World!`

Modify Strings

The upper() method returns the string in upper case:

`a = "Hello, World!"`

`print(a.upper()) # HELLO, WORLD!`

The strip() method removes any whitespace from the beginning or the end:

`a = " Hello, World! "`

`print(a.strip()) # "Hello, World!"`

The replace() method replaces a string with another string:

`a = "Hello, World!"`

`print(a.replace("H", "J")) # Jello, World!`

The split() method splits the string into substrings if it finds instances of the separator:

`a = "Hello, World!"`

`print(a.split(",")) # ['Hello', ' World!']`

String Concatenation

Merge variable a with variable b into variable c:

`a = "Hello"`

`b = "World"`

`c = a + b`

`print(c) # HelloWorld`

String Format

we cannot combine strings and numbers like this:

`age = 36`

`txt = "My name is John, I am " + age`

But we can combine strings and numbers by using the format() method!

The format() method takes unlimited number of arguments, and are placed into the respective placeholders

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

`age = 36`

`txt = "My name is John, and I am {}"`

`print(txt.format(age)) # My name is John, and I am 36`

You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

`quantity = 3`

`itemno = 567`

`price = 49.95`

`myorder = "I want to pay {2} dollars for {0} pieces of item {1}."`

`print(myorder.format(quantity, itemno, price)) # I want to pay 49.95 dollars for 3 pieces of item 567.`

Escape Character

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes

To fix this problem, use the escape character \":

`txt = "We are the so-called \"Vikings\" from the north."`

|Code	| Result    |
| --- | --- |
|\\'	|Single Quote	|
|\\\	|Backslash	|
|\n	|New Line	|
|\r	|Carriage Return	|
|\t	|Tab	|
|\b	|Backspace|

### Booleans
---
Booleans represent one of two values: True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

### Operators
---
Operators are used to perform operations on variables and values.

Arithmetic operators are used with numeric values to perform common mathematical operations:

|Operator|	Name|	
| --- | --- |
|+	|Addition|
|-	|Subtraction|
|*	|Multiplication|
|/	|Division|
|%	|Modulus|
|**	|Exponentiation|
|//	|Floor division|

Assignment operators are used to assign values to variables:

|Operator	|Example	|Same As|
| --- | --- | --- |
|=	|x = 5	|x = 5	|
|+=	|x += 3	|x = x + 3	|
|-=	|x -= 3	|x = x - 3	|
|*=	|x *= 3	|x = x * 3	|
|/=	|x /= 3	|x = x / 3	|
|%=	|x %= 3	|x = x % 3	|
|//=	|x //= 3	|x = x // 3	|
|**=	|x **= 3	|x = x ** 3	|
|&=	|x &= 3	|x = x & 3	|
||=	|x |= 3	|x = x | 3	|
|^=	|x ^= 3	|x = x ^ 3	|
|>>=	|x >>= 3	|x = x >> 3	|
|<<=	|x <<= 3	|x = x << 3|

Comparison operators are used to compare two values:


|Operator	|Name|
| --- | --- |
|==	|Equal|
|!=	|Not equal|
|>	|Greater than|
|<	|Less than|
|>=	|Greater than or equal to|
|<=	|Less than or equal to|

Logical operators are used to combine conditional statements:

|Operator	|Description	|
| --- | --- |
|and 	|Returns True if both statements are true|	
|or	|Returns True if one of the statements is true	|
|not	|Reverse the result, returns False if the result is true|

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

|Operator	|Description	|
| --- | --- |
|is 	|Returns True if both variables are the same object	|
|is not	|Returns True if both variables are not the same object|

Membership operators are used to test if a sequence is presented in an object:


|Operator	|Description	|
| --- | --- |
|in 	|Returns True if a sequence with the specified value is present in the object|
|not in	|Returns True if a sequence with the specified value is|

Bitwise operators are used to compare (binary) numbers:

|Operator	|Name   |Description	|
| --- | --- | --- |
|& 	|AND	|Sets each bit to 1 if both bits are 1|
| \|	|OR	|Sets each bit to 1 if one of two bits is 1|
| ^	|XOR	|Sets each bit to 1 if only one of two bits is 1|
|~ 	|NOT	|Inverts all the bits|
|<<	|Zero fill left shift	|Shift left by pushing zeros in from the right and let the leftmost bits fall off|
|>>	|Signed right shift	|Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off|

### Python Collections (Arrays)
---

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

### Lists
---
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data.

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Since lists are indexed, lists can have items with the same value.

To determine how many items a list has, use the len() function.

List items can be of any data type.

A list can contain different data types.

From Python's perspective, lists are defined as objects with the data type 'list'.

List items are indexed and you can access them by referring to the index number.

-1 refers to the last item, -2 refers to the second last item etc.

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

The first item has index 0.

To determine if a specified item is present in a list use the in keyword.

To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

`thislist = ["apple", "banana", "cherry"]`

`thislist.insert(2, "watermelon")`

`print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']`

To add an item to the end of the list, use the append() method:

`thislist = ["apple", "banana", "cherry"]`

`thislist.append("orange")`

`print(thislist)`

The remove() method removes the specified item.

`thislist = ["apple", "banana", "cherry"]`

`thislist.remove("banana")`

`print(thislist)`

The pop() method removes the specified index.

If you do not specify the index, the pop() method removes the last item.

The del keyword also removes the specified index:

The clear() method empties the list.

The list still remains, but it has no content.

The *iterable* can be any iterable object, like a list, tuple, set etc.

You can use the range() function to create an iterable:

`newlist = [x for x in range(10)]`

List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Sort the list alphabetically:

`thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]`

`thislist.sort()`

`print(thislist)`

Sort the list numerically:

`thislist = [100, 50, 65, 82, 23]`

`thislist.sort()`

`print(thislist)`

To sort descending, use the keyword argument reverse = True:

`thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]`

`thislist.sort(reverse = True)`

`print(thislist)`

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().

`thislist = ["apple", "banana", "cherry"]`

`mylist = thislist.copy()`

`print(mylist)`

Another way to make a copy is to use the built-in method list().

`thislist = ["apple", "banana", "cherry"]`

`mylist = list(thislist)`

`print(mylist)`

There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

`list1 = ["a", "b", "c"]`

`list2 = [1, 2, 3]`

`list3 = list1 + list2`

`print(list3)`

Or you can use the extend() method, which purpose is to add elements from one list to another list:

`list1 = ["a", "b" , "c"]`

`list2 = [1, 2, 3]`

`list1.extend(list2)`

`print(list1)`

### Tuples
---
Tuples are used to store multiple items in a single variable.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

`thistuple = ("apple", "banana", "cherry")`

`print(thistuple) # ("apple", "banana", "cherry")`

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Since tuples are indexed, they can have items with the same value

To determine how many items a tuple has, use the len() function:

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

`thistuple = ("apple",)`

`print(type(thistuple))`

`#NOT a tuple`

`thistuple = ("apple")`

`print(type(thistuple))`

Tuple items can be of any data type, e.g. (String, int and boolean data types).

A tuple can contain different data types

Tuples can be accessed the same way as Lists due to them being indexed as well.

Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


`x = ("apple", "banana", "cherry")`

`y = list(x)`

`y[1] = "kiwi"`

`x = tuple(y)`

`print(x)`

Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.


`thistuple = ("apple", "banana", "cherry")`

`y = ("orange",)`

`thistuple += y`

`print(thistuple)`

When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

`fruits = ("apple", "banana", "cherry")`

`(green, yellow, red) = fruits`

`print(green) # apple`

`print(yellow) # banana`

`print(red) # cherry`

If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

`fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")`

`(green, yellow, *red) = fruits`

`print(green)`

`print(yellow)`

`print(red)`

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

`fruits = ("apple", "mango", "papaya", "pineapple", "cherry")`

`(green, *tropic, red) = fruits`

`print(green)`

`print(tropic)`

`print(red)`

the output for individual variables is String and the variables left are a List

To join two or more tuples you can use the + operator

Built in methods for tuples

|Method	|Description|
| --- | --- |
|count()	|Returns the number of times a specified value occurs in a tuple|
|index()	|Searches the tuple for a specified value and returns the position of where it was found|

### Sets
---
Sets are used to store multiple items in a single variable.

A set is a collection which is unordered, unchangeable*, and unindexed.

Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

`thisset = {"apple", "banana", "cherry"}`

`print(thisset)`

Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Set items can be of any data type

A set can contain different data types

To add one item to a set use the add() method.

To add items from another set into the current set, use the update() method.

`thisset = {"apple", "banana", "cherry"}`

`tropical = {"pineapple", "mango", "papaya"}`

`thisset.update(tropical)`

`print(thisset)`

The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

To remove an item in a set, use the remove(), or the discard() method.

Note: If the item to remove does not exist, remove() will raise an error.

Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.

Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

The clear() method empties the set

The del keyword will delete the set completely

The union() method returns a new set with all items from both sets:

`set1 = {"a", "b" , "c"}`

`set2 = {1, 2, 3}`

`set3 = set1.union(set2)`

`print(set3)`

Note: Both union() and update() will exclude any duplicate items.

The intersection_update() method will keep only the items that are present in both sets

`x = {"apple", "banana", "cherry"}`

`y = {"google", "microsoft", "apple"}`

`x.intersection_update(y)`

`print(x)`

The intersection() method will return a new set, that only contains the items that are present in both sets.

The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

### Dictionaries
---

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets

`thisdict = {`

`  "brand": "Ford",`

`  "model": "Mustang",`

`  "year": 1964`

`}`

`print(thisdict)`

Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

`thisdict = {`

`  "brand": "Ford",`

`  "model": "Mustang",`

`  "year": 1964`

`}`

`print(thisdict["brand"])`

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Dictionaries cannot have two items with the same key

To determine how many items a dictionary has, use the len() function

The values in dictionary items can be of any data type

From Python's perspective, dictionaries are defined as objects with the data type 'dict'

You can access the items of a dictionary by referring to its key name, inside square brackets

`thisdict = {`

`  "brand": "Ford",`

`  "model": "Mustang",`

`  "year": 1964`

`}`

`x = thisdict["model"]`

There is also a method called get() that will give you the same result

`x = thisdict.get("model")`

The keys() method will return a list of all the keys in the dictionary

`x = thisdict.keys()`

Add a new item to the original dictionary, and see that the keys list gets updated as well:

`car = {`

`"brand": "Ford",`

`"model": "Mustang",`

`"year": 1964`

`}`

`x = car.keys()`

`print(x) #before the change`

`car["color"] = "white"`

`print(x) #after the change`

You can change the value of a specific item by referring to its key name:

The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

There are several methods to remove items from a dictionary

The pop() method removes the item with the specified key name

The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)

The del keyword removes the item with the specified key name

The del keyword can also delete the dictionary completely

The clear() method empties the dictionary

You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Another way to make a copy is to use the built-in function dict().

A dictionary can contain dictionaries, this is called nested dictionaries.

