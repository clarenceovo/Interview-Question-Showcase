import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
class canvas:

    def __init__(self,width,height):
        if (width is None ) or (height is None):
            print("Width and height is not provided")
            raise Exception
        logger.debug("Created Canvas board")
        logger.debug(f'Width:{width}. Height:{height}')
        self.__init_width = width
        self.__init_height = height
        self.board = self.create_board(self.__init_width,self.__init_height)

    def create_board(self,width,height):
        """
        Initialize the canvas in multidimenional list filled with ' '
        """
        ret = []
        logger.debug("creating board")
        for _ in range(0,height):
            tmp = []
            for _ in range(0,width):
                tmp.append(' ')
            ret.append(tmp)
        return ret

    def get_canvas_pixel(self,x_corr,y_corr):
        return self.board[y_corr-1][x_corr-1]

    def draw_pixel(self,x_corr,y_corr,patterns='x'):
        if self.board is not None:
            if x_corr > self.__init_width or y_corr > self.__init_height:
                print("Your drawing is out of range")
                raise Exception
            else:
                try:
                    if x_corr >0 and y_corr >0:
                        self.board[y_corr-1][x_corr-1]=patterns
                    else:
                        print("X and Y Coordinate must be greater than 0 ")
                        raise Exception
                except Exception as err:
                    print(err)
        else:
            print("Please create the canvas first")


    def print_canvas(self):
        width_line = ''.join(['-' for item in range(0,self.__init_width)])
        canvas_str = ''
        for row in range(self.__init_height):
            tmp_str = ''.join(self.board[row])
            canvas_str += f'|{tmp_str}|\n'
        ret_str =\
f"""
{width_line}\n{canvas_str}{width_line}
"""
        print(ret_str)
        return
