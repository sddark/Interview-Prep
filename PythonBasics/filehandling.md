File Handling

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

The open() function returns a file object, which has a read() method for reading the content of the file:

By default the read() method returns the whole text, but you can also specify how many characters you want to return:

You can return one line by using the readline() method:

By looping through the lines of the file, you can read the whole file, line by line:

`f = open("demofile.txt", "r")`

`for x in f:`

`>  print(x)`

It is a good practice to always close the file when you are done with it.