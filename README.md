# bored.py
bored.py is a Python module that generates a formatted board or table from a 2D array, displaying row numbers and column letters. It is designed to dynamically adjust to an unlimited number of rows, while supporting up to 26 columns.

This module is specifically designed to facilitate the development of terminal-based board games. As a result, its functionality is not guaranteed when used in GUI-based board games.
## Usage/Examples
To use bored.py in your program, ensure that the file is located within the program's directory and that the module is properly imported:
```python
import bored.py
```
Next, provide the program with the board argument, which should be a 2D array of strings:
```python
list = [
        ['1','2','3'],
        ['1','2','3'],
        ['1','2','3']
]
```
Finally, you can run the module with the following command, ensuring that you provide the 'board' keyword argument:
```python
bored.makeboard(board=list)
```

