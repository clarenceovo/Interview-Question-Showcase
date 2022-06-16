__Project Description__

To begin , please run the following command to install the required library
<br>

```pip install -r requirements.txt```
<br>

To start painting in the canvas, please run the following command to start the drawing console.

```python app.py```

Command 		Description


C w h           Should create a new canvas of width w and height h.

L x1 y1 x2 y2   Should create a new line from (x1,y1) to (x2,y2). Currently only
                horizontal or vertical lines are supported. Horizontal and vertical lines
                will be drawn using the 'x' character.
                
R x1 y1 x2 y2   Should create a new rectangle, whose upper left corner is (x1,y1) and
                lower right corner is (x2,y2). Horizontal and vertical lines will be drawn
                using the 'x' character.
                
B x y c         Should fill the entire area connected to (x,y) with "colour" c. The
                behavior of this is the same as that of the "bucket fill" tool in paint
                programs.
                
Q               Should quit the program.



__Testing__

The unit testing leverages the PyTest Framework to compare the input and result defined in the folder "testcase".
<br>
To run the testcase (in Windows OS) , please run the .cmd file 
<br>
To run the testcase in Linux OS, please run the following command

```
chmod +x run_test_linux.sh

./run_test_linux.sh
```