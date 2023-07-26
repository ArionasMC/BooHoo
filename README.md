# BooHoo
A Python Interpreter for my Turing-complete esolang BooHoo

BooHoo is a turing-complete esolang named after the sound someone makes while trying to code in it. Its uniqueness is based on the fact that all keywords are variations of the words "boo" and "hoo" and also that it has a 3 dimensional memory space (100x100x100, 4GB of memory can be used). 

## BooHoo Language
BooHoo tries to simulate a Turing Machine so you have to keep in mind that there is always an active memory cell. You can change the active cell, increase/decrease or print its value, get input and save it to the cell. Last but not least, you can make a loop that lasts as long as the cell's value is above zero (that can also be used as an if statement).

The starting active cell is at (0, 0, 0). The coordinates have to be at the **[0, 100] range**!

Below is a list of all BooHoo's keywords and their meaning:

**Movement keywords**
```
- hoo: active cell moves front (1, 0, 0)
- ooh: active cell moves back (-1, 0, 0)
- boo: active cell moves up (0, 0, 1)
- oob: active cell moves down (0, 0, -1)
- Boo: active cell moves right (0, 1, 0)
- Hoo: active cell moves left (0, -1, 0)
```
**Change-Value keywords**
```
- bOO: increases the value of the active cell by 1
- HOo: decreases the value of the active cell by 1
```
**Note**: The above keywords have a unique feature, they move the active cell or change its valyue by 'ther length - 2'. For example:
```
- Booo: active cell moves right by 4-2 = 2
- oooooooob: active cell moves down by 9-2 = 7
- bOOOO: increases the value of the active cell by 5-2 = 3
- HOooooo: decreases the value of the active cell by 7-2 = 5
```
You can keep appending 'O' or 'o' respectively to avoid writing those commands tons of times
**I/O keywords**
```
- HOO: requests input and saves it into the active cell
- BOO: prints the value of the active cell
```
**While loop keywords**
```
- bOo: start of loop, think of it like: 'while(active cell value > 0) {'
- HoO: end of loop '}'
```

**Demos**

There are a few demo boohoo programs in _boohoo_demos_ folder along with comments for their explanation. More coming soon.

## BooHoo Interpreter ##
The interpreter is written in Python 3.11 and uses the NumPy library for the 3-d memory space. To run a _.boohoo_ file:
1) Run the main file using ```py main.py```
2) Type the file name with or without the _.boohoo_ extension
   
**Note 1**: The starting directory is the main file's directory. So if you want to run a program from the _boohoo_demos_ folder you have to type ```boohoo_demos/my_program.boohoo```

**Note 2**: A more simple way to run BooHoo programs will be implemented soon
