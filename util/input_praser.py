import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class input_parser:
    def __init__(self):
        self.input_requirement={
            "C":[int,int],
            "L":[int,int,int,int],
            "R":[int,int,int,int],
            "B":[int,int,str],
            "Q":[]
        }
        self.command_key = self.input_requirement.keys()


    def parse_input(self,input_str):
        cmd_list = input_str.split(' ')

        if '' in cmd_list:
            cmd_list.remove('')

        if len(cmd_list)>0:
            cmd_list[0] = cmd_list[0].upper()
            cmd =cmd_list[0]
            if cmd not in self.command_key:
                print("ERROR: The Command is not available")
            else:
                #print("Is a valid command")
                req_input = self.input_requirement[cmd]

                if len(cmd_list) != len(req_input)+1:
                    print("The input format is invaild")
                    raise Exception

                try:
                    for idx in range(1,len(cmd_list)):
                        if req_input[idx-1] is int:
                            cmd_list[idx] = int(cmd_list[idx])

                    return cmd_list
                except:
                    print("Wrong Input Type")