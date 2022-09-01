### Functions
---
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

In Python a function is defined using the def keyword:

`def my_function():`

`>  print("Hello from a function")`

To call a function, use the function name followed by parenthesis:

`def my_function():`

`>  print("Hello from a function")`

`my_function()`

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

`def my_function(fname, lname):`

`>  print(fname + " " + lname)`

`my_function("Emil", "Refsnes")`

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

`def my_function(*kids):`

`>  print("The youngest child is " + kids[2])`

`my_function("Emil", "Tobias", "Linus")`

You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

`def my_function(child3, child2, child1):`

`>  print("The youngest child is " + child3)`

`my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")`

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

`def my_function(**kid):`

`>  print("His last name is " + kid["lname"])`

`my_function(fname = "Tobias", lname = "Refsnes")`

The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

`def my_function(country = "Norway"):`

`>  print("I am from " + country)`

`my_function()`

To let a function return a value, use the return statement:

`def my_function(x):`

`>  return 5 * x`

`print(my_function(3))`

function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

`def myfunction():`

`>  pass`

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.