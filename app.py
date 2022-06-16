import logging
import sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from canvas.canvas import canvas
from util.input_praser import input_parser
class draw_something:
    def __init__(self):
        logger.debug("Started the draw_something class")
        self.is_running = True
        self.canvas = None
        self.parser = input_parser()
        self.recursion_count = 0
        self.recursion_check = []

    def create_canvas(self,width,height):

        if width > 0 and height > 0:
            self.canvas = canvas(width, height)
            self.canvas_width = width
            self.canvas_height = height
            sys.setrecursionlimit(100000)
        else:
            print("The width and height of canvas must be greater than 0")

    def draw_lines(self,start_point:tuple,end_point:tuple):
        """
        Draw straight horizontal lines or vertical lines for function "L"
        """
        if start_point[1] == end_point[1]:
            #Horizontal Line
            #print(f"Drawing Horizontal Lines from {start_point} to {end_point}")
            for idx in range(start_point[0],end_point[0]+1):
                self.canvas.draw_pixel(idx,start_point[1])

        elif  start_point[0] == end_point[0]:
            # Vertical Line
            #print(f"Drawing Vertical Lines from {start_point} to {end_point}")
            for idx in range(start_point[1],end_point[1]+1):
                self.canvas.draw_pixel(start_point[0],idx)

        else:
            print("Please draw either horizontal or vertical lines")

    def draw_rectangle(self,start_point:tuple,end_point:tuple):
        if (start_point[0] > end_point[0]) or (start_point[1]>start_point[1]):
            print("The start point and end point of the input cannot construct a rectangle")
            return
        if (start_point[0] <=0 or  end_point[0] <=0) or (start_point[1] <=0 > start_point[1]<=0):
            print("The X and Y Coordinate of start point and/or end point must be greater than 0 ")
            return
        else:
            #print(start_point)
            #print(end_point)
            for y_corr in range(start_point[1],end_point[1]+1):
                #print(y_corr)
                for x_corr in range(start_point[0],end_point[0]+1):
                    #print(x_corr)
                    if x_corr not in [start_point[0],end_point[0]] and y_corr not in [start_point[1],end_point[1]]:
                        pass
                    else:
                        self.canvas.draw_pixel(x_corr, y_corr)

    def recursive_fill(self,x_corr:int,y_corr:int ,pattern:str):
        self.recursion_count+=1 #for test
        self.recursion_check.append((x_corr,y_corr))

        """
        Flood Algo with O(NM) ,Where n is the width and m is the height of the canvas
        """
        if x_corr < 1 or x_corr > self.canvas_width or y_corr < 1 or y_corr> self.canvas_height :
            return
        else:
            check_mark = self.canvas.get_canvas_pixel(x_corr,y_corr)
            if check_mark == "x":
                return
            else:
                self.canvas.draw_pixel(x_corr, y_corr,pattern)

                #Flood Algo Function
                if x_corr +1 <=self.canvas_width and (x_corr+1,y_corr) not in self.recursion_check:
                    self.recursive_fill(x_corr+1,y_corr,pattern)

                if x_corr -1 >0 and not (x_corr-1,y_corr) in self.recursion_check:
                    #print(x_corr)
                    self.recursive_fill(x_corr-1,y_corr,pattern)

                if y_corr +1 <=self.canvas_height and (x_corr,y_corr+1) not in self.recursion_check:
                    self.recursive_fill(x_corr,y_corr+1,pattern)

                if y_corr -1 >0 and not (x_corr,y_corr-1) in self.recursion_check:
                    self.recursive_fill(x_corr,y_corr-1,pattern)


    def blackfill_canvas(self,start_point:tuple,pattern:str):
        """
        Use recurcisve method to blackfill the canvas
        """
        if self.canvas_width < start_point[0] or self.canvas_height < start_point[1] < start_point[1]:
            print("Your drawing is out of range")
            return

        self.recursive_fill(start_point[0],start_point[1],pattern)
        #print(self.recursion_count) #for test
        #self.recursion_check.clear() #for test


    def quit(self):
        self.is_running = False
        print("Byebye!~")

    def run(self):
        """
        Main function to get the input from the console
        1. Parse the input by ths praser function
        2. Execute the control function and update the canvas
        3. Execute the canvas print function to output the canvas
        4. When receive "End" signal , terminate the loop

        :return:
        """
        #self.create_canvas(20, 4)  # for test
        #self.draw_rectangle((14,1), (18,3)) # for test
        while self.is_running:
            try:
                input_argv = input("Please type the command:")
                cmd_list = self.parser.parse_input(input_argv)
                cmd = cmd_list[0]

                if cmd == "Q":
                    self.quit()
                    return 0
                elif cmd == "L":
                    #print("Drawing Lines ")
                    start = (cmd_list[1],cmd_list[2])
                    end = (cmd_list[3],cmd_list[4])
                    self.draw_lines(start,end)

                elif cmd == "R":
                    start = (cmd_list[1],cmd_list[2])
                    end = (cmd_list[3],cmd_list[4])
                    self.draw_rectangle(start,end)

                elif cmd == "B":
                    start = (cmd_list[1],cmd_list[2])
                    self.blackfill_canvas(start,cmd_list[3])

                elif cmd == "C":
                    self.create_canvas(cmd_list[1],cmd_list[2])

                if self.canvas is not None:
                    self.canvas.print_canvas()

            except Exception as err:
                continue

def main_function():
    logger.debug("Started the main")
    draw_console = draw_something()
    draw_console.run()

if __name__ == '__main__':
    main_function()